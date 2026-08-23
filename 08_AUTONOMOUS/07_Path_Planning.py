# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 07 - ODOMETRY PATH PLANNING
# ============================================================

from vex import *
from math import sin, cos, radians, degrees, atan2, sqrt


brain = Brain()

left_drive = MotorGroup(
    Motor(Ports.PORT1, GearSetting.RATIO_18_1, False),
    Motor(Ports.PORT2, GearSetting.RATIO_18_1, False),
    Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
)

right_drive = MotorGroup(
    Motor(Ports.PORT8, GearSetting.RATIO_18_1, True),
    Motor(Ports.PORT9, GearSetting.RATIO_18_1, True),
    Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
)

left_tracking = Rotation(Ports.PORT6)
right_tracking = Rotation(Ports.PORT7)
imu = Inertial(Ports.PORT5)


# ------------------------------------------------------------
# PATH
# ------------------------------------------------------------
#
# Path'i waypoint'lerden oluşturuyoruz.
#
# Robot:
#
# (0, 0)
#   ↓
# (500, 0)
#   ↓
# (500, 500)
#   ↓
# (1000, 500)
#
# noktalarından sırayla geçecek.
#
# X → saha üzerindeki sağ-sol konum
# Y → başlangıç yönündeki ileri-geri konum
# ------------------------------------------------------------

PATH = [
    (500, 0),
    (500, 500),
    (1000, 500)
]


# ------------------------------------------------------------
# ODOMETRY AYARLARI
# ------------------------------------------------------------

WHEEL_DIAMETER = 50
WHEEL_CIRCUMFERENCE = 3.14159 * WHEEL_DIAMETER

x = 0
y = 0

last_left = 0
last_right = 0


# ------------------------------------------------------------
# PID / CONTROL AYARLARI
# ------------------------------------------------------------

TURN_KP = 0.8
DRIVE_KP = 0.25
HEADING_KP = 1.0

POSITION_TOLERANCE = 25
HEADING_TOLERANCE = 1


# ------------------------------------------------------------
# ODOMETRY
# ------------------------------------------------------------
#
# VEX heading:
#
# 0° → başlangıç yönü
# Heading saat yönünde artar.
#
# Bu nedenle:
#
#     X hareketi = distance × sin(heading)
#     Y hareketi = distance × cos(heading)
#
# kullanıyoruz.
# ------------------------------------------------------------

def reset_odometry():
    global x, y, last_left, last_right

    x = 0
    y = 0

    left_tracking.reset_position()
    right_tracking.reset_position()

    last_left = left_tracking.position(DEGREES)
    last_right = right_tracking.position(DEGREES)


def update_odometry():
    global x, y, last_left, last_right

    current_left = left_tracking.position(DEGREES)
    current_right = right_tracking.position(DEGREES)

    left_delta = current_left - last_left
    right_delta = current_right - last_right

    left_distance = left_delta / 360 * WHEEL_CIRCUMFERENCE
    right_distance = right_delta / 360 * WHEEL_CIRCUMFERENCE

    forward_distance = (left_distance + right_distance) / 2

    heading = radians(imu.heading(DEGREES))

    x += forward_distance * sin(heading)
    y += forward_distance * cos(heading)

    last_left = current_left
    last_right = current_right


# ------------------------------------------------------------
# AÇI HATASI
# ------------------------------------------------------------
#
# Örneğin:
#
# Target = 5°
# Current = 355°
#
# Normal çıkarma 350° verir.
# Halbuki robotun yalnızca 10° dönmesi gerekir.
#
# Bu fonksiyon açıyı -180° ile +180° arasına getirir.
# ------------------------------------------------------------

def angle_error(target, current):
    error = target - current

    while error > 180:
        error -= 360

    while error < -180:
        error += 360

    return error


# ------------------------------------------------------------
# TURN TO HEADING
# ------------------------------------------------------------
#
# Robot önce waypoint'e doğru bakacak şekilde döner.
# Burada basit bir P kontrolü kullanıyoruz.
#
# Büyük hata → daha fazla motor gücü
# Küçük hata → daha az motor gücü
# ------------------------------------------------------------

def turn_to_heading(target_heading):
    while True:
        current_heading = imu.heading(DEGREES)
        error = angle_error(target_heading, current_heading)

        output = TURN_KP * error

        if output > 60:
            output = 60

        if output < -60:
            output = -60

        if abs(error) <= HEADING_TOLERANCE:
            break

        if output > 0:
            left_drive.spin(FORWARD, output, PERCENT)
            right_drive.spin(REVERSE, output, PERCENT)
        else:
            left_drive.spin(REVERSE, abs(output), PERCENT)
            right_drive.spin(FORWARD, abs(output), PERCENT)

        wait(20, MSEC)

    left_drive.stop(BRAKE)
    right_drive.stop(BRAKE)


# ------------------------------------------------------------
# GO TO WAYPOINT
# ------------------------------------------------------------
#
# Önce:
#
#     Hedef nokta nerede?
#
# Sonra:
#
#     Robotun oraya bakması için gereken heading nedir?
#
# Daha sonra robot o yöne dönüp ileri hareket eder.
#
# Robot hareket ederken heading'i tekrar kontrol eder ve
# küçük sapmaları düzeltir.
# ------------------------------------------------------------

def go_to(target_x, target_y):
    while True:
        update_odometry()

        dx = target_x - x
        dy = target_y - y

        distance_to_target = sqrt(dx * dx + dy * dy)

        if distance_to_target <= POSITION_TOLERANCE:
            break

        target_heading = degrees(atan2(dx, dy))

        if target_heading < 0:
            target_heading += 360

        heading_error = angle_error(
            target_heading,
            imu.heading(DEGREES)
        )

        correction = HEADING_KP * heading_error

        drive_speed = DRIVE_KP * distance_to_target

        if drive_speed > 60:
            drive_speed = 60

        if drive_speed < 15:
            drive_speed = 15

        left_speed = drive_speed + correction
        right_speed = drive_speed - correction

        if left_speed > 100:
            left_speed = 100

        if left_speed < -100:
            left_speed = -100

        if right_speed > 100:
            right_speed = 100

        if right_speed < -100:
            right_speed = -100

        left_drive.spin(FORWARD, left_speed, PERCENT)
        right_drive.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)

    left_drive.stop(BRAKE)
    right_drive.stop(BRAKE)


# ------------------------------------------------------------
# AUTONOMOUS
# ------------------------------------------------------------

def autonomous():
    reset_odometry()

    for waypoint in PATH:
        go_to(waypoint[0], waypoint[1])

    left_drive.stop(BRAKE)
    right_drive.stop(BRAKE)


# ------------------------------------------------------------
# BAŞLANGIÇ AYARLARI
# ------------------------------------------------------------

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.set_heading(0, DEGREES)


# Autonomous'u çalıştır.

autonomous()


# ============================================================
# Ders 07 bitti, bir sonraki derse geçin.
# END OF 07 - ODOMETRY PATH PLANNING
# ============================================================