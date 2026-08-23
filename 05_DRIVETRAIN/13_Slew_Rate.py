# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 13 - SLEW RATE
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


# Slew Rate, motor hızının ne kadar hızlı değişebileceğini
# sınırlar.
#
# Örneğin joystick bir anda %100'e çıktığında motoru da
# doğrudan %100 yapmak yerine hızını kademeli olarak artırırız.
#
# Bu, ani kalkışları ve tekerleklerin patinaj yapmasını
# azaltmaya yardımcı olabilir.

SLEW_STEP = 5

left_speed = 0
right_speed = 0


while True:
    target_left = controller.axis3.position()
    target_right = controller.axis2.position()

    if left_speed < target_left:
        left_speed = min(left_speed + SLEW_STEP, target_left)
    elif left_speed > target_left:
        left_speed = max(left_speed - SLEW_STEP, target_left)

    if right_speed < target_right:
        right_speed = min(right_speed + SLEW_STEP, target_right)
    elif right_speed > target_right:
        right_speed = max(right_speed - SLEW_STEP, target_right)

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)


# ============================================================
# Ders 13 bitti, bir sonraki derse geçin.
# END OF 13 - SLEW RATE
# ============================================================