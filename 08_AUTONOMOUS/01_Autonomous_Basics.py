# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 01 - AUTONOMOUS BASICS
# ============================================================

from vex import *


brain = Brain()

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
# AUTONOMOUS NEDİR?
# ------------------------------------------------------------
#
# Autonomous dönemde robotu sürücü kontrol etmez.
# Önceden yazdığımız program robotun hangi hareketleri
# yapacağını belirler.
#
# Örneğin:
#
#     500 mm ileri git
#     90° dön
#     tekrar 300 mm git
#
# Program bu hareketleri sırasıyla uygular.
#
# Autonomous'un amacı yalnızca robotu hareket ettirmek değil,
# bunu mümkün olduğunca güvenilir ve tekrarlanabilir
# şekilde yapmaktır.
# ------------------------------------------------------------


# ------------------------------------------------------------
# BASİT BİR AUTONOMOUS
# ------------------------------------------------------------
#
# Önce 500 mm ileri gidiyoruz.
# drive_for() tamamlanana kadar program bir sonraki satıra
# geçmez.
# ------------------------------------------------------------

drivetrain.set_drive_velocity(50, PERCENT)
drivetrain.set_turn_velocity(40, PERCENT)
drivetrain.set_stopping(BRAKE)

drivetrain.drive_for(FORWARD, 500, MM)

drivetrain.turn_for(RIGHT, 90, DEGREES)

drivetrain.drive_for(FORWARD, 300, MM)

drivetrain.stop()


# ------------------------------------------------------------
# AUTONOMOUS'U NASIL DÜŞÜNMELİYİZ?
# ------------------------------------------------------------
#
# Autonomous'u bir hareket dizisi olarak düşünebiliriz:
#
#     Hareket 1
#        ↓
#     Hareket 2
#        ↓
#     Hareket 3
#        ↓
#     Görev tamamlandı
#
# Örneğin bir oyun nesnesine gitmek için:
#
#     İleri git
#     Dön
#     Mekanizmayı çalıştır
#     Geri dön
#
# şeklinde bir sıra oluşturabiliriz.
#
# İleride sensörler ve PID kullanarak bu hareketleri
# daha hassas ve daha güvenilir hale getireceğiz.
# ------------------------------------------------------------


# ============================================================
# Ders 01 bitti, bir sonraki derse geçin.
# END OF 01 - AUTONOMOUS BASICS
# ============================================================