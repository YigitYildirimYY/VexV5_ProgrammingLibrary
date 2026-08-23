# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 02 - TANK DRIVE
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
# TANK DRIVE NEDİR?
# ------------------------------------------------------------
#
# Tank Drive'da sol ve sağ motor grupları birbirinden bağımsız
# kontrol edilir.
#
# Sol joystick → sol taraf
# Sağ joystick → sağ taraf
#
# İki joystick aynı yönde hareket ederse robot düz gider.
# İki joystick zıt yönde hareket ederse robot döner.
# ------------------------------------------------------------


while True:
    left_speed = controller.axis3.position()
    right_speed = controller.axis2.position()

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)


# ============================================================
# Ders 02 bitti, bir sonraki derse geçin.
# END OF 02 - TANK DRIVE
# ============================================================