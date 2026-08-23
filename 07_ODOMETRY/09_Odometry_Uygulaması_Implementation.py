# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 09 - ODOMETRY IMPLEMENTATION
# ============================================================

from vex import *
from math import sin, cos, radians


brain = Brain()

left_tracking = Rotation(Ports.PORT7)
right_tracking = Rotation(Ports.PORT8)
imu = Inertial(Ports.PORT9)


# ------------------------------------------------------------
# ODOMETRY IMPLEMENTATION
# ------------------------------------------------------------
#
# Bu örnekte iki tracking wheel ve bir IMU kullanıyoruz.
#
# Tracking wheel'ler robotun ne kadar hareket ettiğini,
# IMU ise robotun heading'ini takip ediyor.
#
# Her güncellemede:
#
# 1. Tracking wheel'lerin ne kadar hareket ettiğini buluyoruz.
# 2. Sol ve sağ wheel'in ortalamasını ileri hareket olarak
#    kabul ediyoruz.
# 3. Heading'i kullanarak bu hareketi X ve Y'ye dağıtıyoruz.
#
# Sonuç olarak robotun:
#
#     X
#     Y
#     Heading
#
# değerlerini sürekli güncelliyoruz.
# ------------------------------------------------------------

wheel_diameter = 50
wheel_circumference = 3.14159 * wheel_diameter

x = 0
y = 0


# Odometry başlamadan önce sensörleri sıfırlıyoruz.

left_tracking.reset_position()
right_tracking.reset_position()

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)


last_left = left_tracking.position(DEGREES)
last_right = right_tracking.position(DEGREES)


# ------------------------------------------------------------
# ODOMETRY UPDATE
# ------------------------------------------------------------
#
# Bu fonksiyon robotun konumunu bir kez günceller.
# Gerçek robot kodunda bunu sürekli çağırırız.
# ------------------------------------------------------------

def update_odometry():
    global x, y, last_left, last_right

    current_left = left_tracking.position(DEGREES)
    current_right = right_tracking.position(DEGREES)

    left_delta = current_left - last_left
    right_delta = current_right - last_right

    left_distance = left_delta / 360 * wheel_circumference
    right_distance = right_delta / 360 * wheel_circumference

    forward_distance = (left_distance + right_distance) / 2

    heading = imu.heading(DEGREES)
    angle = radians(heading)

    global_x = forward_distance * cos(angle)
    global_y = forward_distance * sin(angle)

    x += global_x
    y += global_y

    last_left = current_left
    last_right = current_right


# ------------------------------------------------------------
# ODOMETRY LOOP
# ------------------------------------------------------------

while True:
    update_odometry()

    brain.screen.clear_screen()
    brain.screen.print("X: ", x)
    brain.screen.next_row()
    brain.screen.print("Y: ", y)
    brain.screen.next_row()
    brain.screen.print("Heading: ", imu.heading(DEGREES))

    wait(20, MSEC)


# ============================================================
# Ders 09 bitti, bir sonraki derse geçin.
# END OF 09 - ODOMETRY IMPLEMENTATION
# ============================================================