# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 14 - DRIVETRAIN GEARING
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
# 1. DRIVETRAIN'DE GEAR RATIO
# ------------------------------------------------------------
#
# Motorun kendi cartridge'ı ile tekerlek arasında ekstra
# dişliler kullanırsak drivetrain'in çıkış hızı ve torku
# değişir.
#
# Genel olarak:
#
# Daha yüksek çıkış hızı → daha hızlı robot
# Daha yüksek çıkış torku → daha güçlü robot
#
# İkisini aynı anda maksimum yapmak mümkün değildir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. EXTERNAL GEAR RATIO
# ------------------------------------------------------------
#
# DriveTrain oluştururken son parametre externalGearRatio'dur.
#
# Dışarıda kullandığımız dişliler drivetrain'in tekerlek
# hareketini değiştiriyorsa bu oran burada belirtilir.
#
# Ekstra bir dış dişli oranı yoksa:
#
#     1.0
#
# kullanılır.
# ------------------------------------------------------------


# Örnek:
# drivetrain = DriveTrain(left_drive, right_drive,
#                         319.19, 320, 40, MM, 1.0)


# ------------------------------------------------------------
# 3. HIZ - TORK DENGESİ
# ------------------------------------------------------------
#
# Örneğin motor ile tekerlek arasında hız düşüren bir
# dişli sistemi kullanırsak tekerlek daha yavaş döner,
# fakat daha fazla tork elde ederiz.
#
# Tersine, hızı artıran bir oran kullanırsak robot daha
# hızlı olabilir fakat tekerlekteki tork azalır.
#
# Bu yüzden drivetrain gearing seçimi robotun kullanım
# amacına göre yapılır.
# ------------------------------------------------------------


# ============================================================
# Ders 14 bitti, bir sonraki derse geçin.
# END OF 14 - DRIVETRAIN GEARING
# ============================================================