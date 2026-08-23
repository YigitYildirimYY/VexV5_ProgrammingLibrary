# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 08 - AUTONOMOUS DEBUGGING
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

imu = Inertial(Ports.PORT9)


# ------------------------------------------------------------
# AUTONOMOUS DEBUGGING NEDİR?
# ------------------------------------------------------------
#
# Autonomous kodu tek tek çalışsa bile bütün rutinde
# beklenmedik sonuçlar çıkabilir.
#
# Debugging'de ilk amacımız kodu değiştirmek değil,
# robotun o anda ne yaptığını görmektir.
#
# Örneğin:
#
# current → robotun mevcut açısı
# error   → hedef açından ne kadar uzaktasın?
#
# Böylece problemin hareketten mi, sensörden mi veya
# hesaplamadan mı kaynaklandığını anlayabiliriz.
# ------------------------------------------------------------


target_heading = 90


# ------------------------------------------------------------
# AUTONOMOUS TEST
# ------------------------------------------------------------

def autonomous():
    imu.reset_rotation()

    left_drive.spin(FORWARD, 30, PERCENT)
    right_drive.spin(REVERSE, 30, PERCENT)

    while True:
        current = imu.rotation(DEGREES)
        error = target_heading - current

        brain.screen.clear_screen()
        brain.screen.print("Heading: ", current)
        brain.screen.next_row()
        brain.screen.print("Error: ", error)

        if abs(error) <= 2:
            break

        wait(20, MSEC)

    left_drive.stop(BRAKE)
    right_drive.stop(BRAKE)


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


# ------------------------------------------------------------
# COMPETITION
# ------------------------------------------------------------

imu.calibrate()

while imu.is_calibrating():
    brain.screen.clear_screen()
    brain.screen.print("Calibrating IMU...")
    wait(50, MSEC)

competition = Competition(driver_control, autonomous)