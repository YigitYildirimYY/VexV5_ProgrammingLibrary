# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 03 - ARCADE DRIVE
# ============================================================

# ArcadeDrive ile Tank arasındaki fark, birinde iki, birinde sadece bir kontrol çubuğuyla robotu kullanıyor olmamızdır,
# Kod açısından çok önemli bir değişiklik olmamakla birlikte, Arcade Drive biraz daha karmaşıktır,
# Robotta Arcade veya Tank olması, driverin tercihine bağlıdır diyebiliriz.

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
# ARCADE DRIVE NEDİR?
# ------------------------------------------------------------
#
# Arcade Drive'da tek joystick ile hem ileri-geri hem de
# dönüş kontrol edilir.
#
# axis3 → İleri / geri
# axis4 → Sağa / sola dönüş
#
# İki değeri birleştirerek sol ve sağ motorların hızını
# hesaplarız.
# ------------------------------------------------------------


while True:
    forward = controller.axis3.position()
    turn = controller.axis4.position()

    left_speed = forward + turn
    right_speed = forward - turn

    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)


# ============================================================
# Ders 03 bitti, bir sonraki derse geçin.
# END OF 03 - ARCADE DRIVE
# ============================================================