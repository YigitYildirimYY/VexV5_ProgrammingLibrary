# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 05 - X-DRIVE
# ============================================================

from vex import *


brain = Brain()
controller = Controller(PRIMARY)

front_left = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
front_right = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
back_left = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
back_right = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)


# ------------------------------------------------------------
# 1. X-DRIVE NEDİR?
# ------------------------------------------------------------
#
# X-Drive, dört omni wheel'in çapraz şekilde yerleştirildiği
# bir drivetrain türüdür.
#
# Tank Drive'dan farklı olarak robot sadece ileri ve geri
# gitmez. Sağa ve sola da hareket edebilir.
#
# Bu yüzden üç temel hareketi vardır:
#
# forward → ileri / geri
# strafe  → sağ / sol
# turn    → kendi etrafında dönme
#
# Bu hareketler aynı anda kullanılabildiği için robot çapraz
# da hareket edebilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. JOYSTICK KONTROLÜ
# ------------------------------------------------------------
#
# Sol joystick:
# axis3 → forward / backward
# axis4 → strafe left / right
#
# Sağ joystick:
# axis1 → turn
# ------------------------------------------------------------

while True:
    forward = controller.axis3.position()
    strafe = controller.axis4.position()
    turn = controller.axis1.position()

    front_left_speed = forward + strafe + turn
    front_right_speed = forward - strafe - turn
    back_left_speed = forward - strafe + turn
    back_right_speed = forward + strafe - turn

    # Aynı anda birkaç hareket yapıldığında hesaplanan motor
    # hızlarından biri 100'ü geçebilir. Oranları koruyarak
    # bütün değerleri 100 sınırına indiriyoruz.

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


# ------------------------------------------------------------
# 3. HAREKET MANTIĞI
# ------------------------------------------------------------
#
# Sadece forward kullanırsak robot ileri veya geri gider.
# Sadece strafe kullanırsak robot yana hareket eder.
# Sadece turn kullanırsak robot kendi etrafında döner.
# forward ve strafe aynı anda verilirse robot çapraz gider.
#
# Üçü aynı anda kullanılırsa robot çapraz hareket ederken
# aynı zamanda dönebilir.
# ------------------------------------------------------------


# ============================================================
# Ders 05 bitti, bir sonraki derse geçin.
# END OF 05 - X-DRIVE
# ============================================================