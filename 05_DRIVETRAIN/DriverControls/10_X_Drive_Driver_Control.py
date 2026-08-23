# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# DriverControls
# 10 - X-DRIVE DRIVER CONTROL
# ============================================================

from vex import *


brain = Brain()
controller = Controller(PRIMARY)

front_left = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
front_right = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
back_left = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
back_right = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)


# X-Drive'da üç hareketi aynı anda kontrol edebiliriz.
#
# axis3 → forward / backward
# axis4 → strafe left / right
# axis1 → turn

while True:
    forward = controller.axis3.position()
    strafe = controller.axis4.position()
    turn = controller.axis1.position()

    front_left_speed = forward + strafe + turn
    front_right_speed = forward - strafe - turn
    back_left_speed = forward - strafe + turn
    back_right_speed = forward + strafe - turn

    max_speed = max(
        100,
        abs(front_left_speed),
        abs(front_right_speed),
        abs(back_left_speed),
        abs(back_right_speed)
    )

    front_left_speed = front_left_speed * 100 / max_speed
    front_right_speed = front_right_speed * 100 / max_speed
    back_left_speed = back_left_speed * 100 / max_speed
    back_right_speed = back_right_speed * 100 / max_speed

    front_left.spin(FORWARD, front_left_speed, PERCENT)
    front_right.spin(FORWARD, front_right_speed, PERCENT)
    back_left.spin(FORWARD, back_left_speed, PERCENT)
    back_right.spin(FORWARD, back_right_speed, PERCENT)

    wait(20, MSEC)


# ============================================================
# Ders 10 bitti, bir sonraki derse geçin.
# END OF 10 - X-DRIVE DRIVER CONTROL
# ============================================================