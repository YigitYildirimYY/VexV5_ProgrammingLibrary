# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 06 - MECANUM DRIVE
# ============================================================

from vex import *


brain = Brain()
controller = Controller(PRIMARY)

front_left = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
front_right = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
back_left = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
back_right = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)


# ------------------------------------------------------------
# 1. MECANUM DRIVE NEDİR?
# ------------------------------------------------------------
#
# Mecanum Drive, dört mecanum wheel kullanan bir drivetrain'dir.
#
# Normal tank drivetrain'den farklı olarak robot:
#
# - ileri / geri
# - sağ / sol
# - kendi etrafında dönüş
#
# hareketlerini birbirinden bağımsız şekilde birleştirebilir.
#
# Bu yüzden robot çapraz yönde de hareket edebilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. JOYSTICK KONTROLÜ
# ------------------------------------------------------------
#
# Sol joystick:
# axis3 → ileri / geri
# axis4 → sağ / sol
#
# Sağ joystick:
# axis1 → dönüş
#
# Controller.axis*.position() -100 ile 100 arasında değer verir.
# ------------------------------------------------------------

while True:
    forward = controller.axis3.position()
    strafe = controller.axis4.position()
    turn = controller.axis1.position()

    front_left_speed = forward + strafe + turn
    front_right_speed = forward - strafe - turn
    back_left_speed = forward - strafe + turn
    back_right_speed = forward + strafe - turn


    # Birkaç hareket aynı anda yapıldığında bazı motor
    # değerleri 100'ü aşabilir. Oranları koruyarak
    # değerleri -100 ile 100 arasında tutuyoruz.

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
# Ders 06 bitti, bir sonraki derse geçin.
# END OF 06 - MECANUM DRIVE
# ============================================================