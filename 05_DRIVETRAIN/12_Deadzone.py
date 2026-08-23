# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 12 - DEADZONE
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


# ------------------------------------------------------------
# DEADZONE NEDİR?
# ------------------------------------------------------------
#
# Joystick'i bıraktığımızda değerin tam olarak 0 olması
# gerekmez. Küçük değerler, örneğin 1 veya -3, gelebilir.
#
# Bu küçük değerler motorların istemeden hafifçe çalışmasına
# neden olabilir.
#
# Deadzone ile belirlediğimiz aralıktaki küçük joystick
# değerlerini 0 kabul ederiz.
# ------------------------------------------------------------

DEADZONE = 10


while True:
    left_speed = controller.axis3.position()
    right_speed = controller.axis2.position()

    if abs(left_speed) < DEADZONE:
        left_speed = 0

    if abs(right_speed) < DEADZONE:
        right_speed = 0

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)


# ============================================================
# Ders 12 bitti, bir sonraki derse geçin.
# END OF 12 - DEADZONE
# ============================================================