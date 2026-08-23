# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 03 - MOVEMENT SEQUENCES
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


# ------------------------------------------------------------
# MOVEMENT SEQUENCE NEDİR?
# ------------------------------------------------------------
#
# Autonomous'u tek tek komutlardan oluşan bir hareket dizisi
# olarak düşünebiliriz.
#
# Örneğin:
#
#     1. İleri git
#     2. Sağa dön
#     3. Tekrar ileri git
#
# Fonksiyon kullanırsak bu hareketleri tek bir görev altında
# toplamak daha düzenli olur.
# ------------------------------------------------------------


def score_routine():
    drivetrain.drive_for(FORWARD, 500, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)


# ------------------------------------------------------------
# AUTONOMOUS
# ------------------------------------------------------------

def autonomous():
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_turn_velocity(40, PERCENT)
    drivetrain.set_stopping(BRAKE)

    score_routine()


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


competition = Competition(driver_control, autonomous)


# ============================================================
# Ders 03 bitti, bir sonraki derse geçin.
# END OF 03 - MOVEMENT SEQUENCES
# ============================================================