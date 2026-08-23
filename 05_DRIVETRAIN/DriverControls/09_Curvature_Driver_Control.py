# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# Driver Controls
# 09 - CURVATURE DRIVER CONTROL
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


# Curvature Drive'da dönüş miktarını robotun ileri-geri
# hızına göre ölçeklendiriyoruz.
#
# axis3 → ileri / geri
# axis4 → dönüş

while True:
    forward = controller.axis3.position()
    turn = controller.axis4.position()

    turn_effect = turn * abs(forward) / 100

    left_speed = forward + turn_effect
    right_speed = forward - turn_effect

    max_speed = max(100, abs(left_speed), abs(right_speed))

    left_speed = left_speed * 100 / max_speed
    right_speed = right_speed * 100 / max_speed

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)


# ============================================================
# Ders 09 bitti, bir sonraki derse geçin.
# END OF 09 - CURVATURE DRIVER CONTROL
# ============================================================