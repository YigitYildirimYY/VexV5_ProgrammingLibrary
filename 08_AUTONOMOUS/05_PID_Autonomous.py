# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 05 - PID AUTONOMOUS
# ============================================================

from vex import *


brain = Brain()
controller = Controller(PRIMARY)

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

drivetrain = DriveTrain(left_drive, right_drive, 319.19, 320, 40, MM, 1.0)

imu = Inertial(Ports.PORT7)


# ------------------------------------------------------------
# TURN PID
# ------------------------------------------------------------
#
# Bu fonksiyon robotu verilen açı kadar döndürür.
#
# Örneğin:
#
#     turn_pid(90)
#
# robotun bulunduğu noktadan 90° dönmesini sağlar.
#
# Buradaki PID değerleri örnektir. Gerçek robot için
# tuning yapılması gerekir.
# ------------------------------------------------------------

def turn_pid(target):
    Kp = 0.6
    Ki = 0.01
    Kd = 0.2

    integral = 0
    previous_error = 0

    imu.reset_rotation()

    while True:
        current = imu.rotation(DEGREES)
        error = target - current

        integral += error
        derivative = error - previous_error

        output = Kp * error + Ki * integral + Kd * derivative

        if output > 100:
            output = 100

        if output < -100:
            output = -100

        if abs(error) <= 1:
            break

        if output > 0:
            left_drive.spin(FORWARD, output, PERCENT)
            right_drive.spin(REVERSE, output, PERCENT)
        else:
            left_drive.spin(REVERSE, abs(output), PERCENT)
            right_drive.spin(FORWARD, abs(output), PERCENT)

        previous_error = error

        wait(20, MSEC)

    left_drive.stop(BRAKE)
    right_drive.stop(BRAKE)


# ------------------------------------------------------------
# AUTONOMOUS
# ------------------------------------------------------------
#
# Burada PID'yi autonomous hareket dizisinin yalnızca
# gerektiği yerde kullanıyoruz.
#
# Her hareketin PID olmak zorunda olmadığını unutma.
# Basit ve güvenilir bir hareket için drive_for() yeterli
# olabilir.
# ------------------------------------------------------------

def autonomous():
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_stopping(BRAKE)

    drivetrain.drive_for(FORWARD, 500, MM)

    turn_pid(90)

    drivetrain.drive_for(FORWARD, 300, MM)

    drivetrain.stop()


# ------------------------------------------------------------
# DRIVER CONTROL
# ------------------------------------------------------------

def driver_control():
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        left_drive.spin(FORWARD, left_speed, PERCENT)
        right_drive.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)


# IMU'yu autonomous veya driver başlamadan önce kalibre ediyoruz.

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)


competition = Competition(driver_control, autonomous)


# ============================================================
# Ders 05 bitti, bir sonraki derse geçin.
# END OF 05 - PID AUTONOMOUS
# ============================================================