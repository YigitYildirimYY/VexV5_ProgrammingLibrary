# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 01 - DRIVETRAIN BASICS
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
# DRIVETRAIN NEDİR?
# ------------------------------------------------------------
#
# Drivetrain, robotun hareket etmesini sağlayan sistemdir.
# Tank drivetrain'de sol ve sağ taraf ayrı ayrı kontrol edilir.
#
# İki taraf aynı yönde çalışırsa robot düz hareket eder.
# İki taraf zıt yönde çalışırsa robot döner.
# ------------------------------------------------------------


# Robotu sürekli ileri sür.

drivetrain.drive(FORWARD)

wait(1, SECONDS)

drivetrain.stop()


# Robotu %50 hızla ileri sür.

drivetrain.drive(FORWARD, 50, PERCENT)

wait(1, SECONDS)

drivetrain.stop()


# Robotu 500 mm ileri götür.

drivetrain.drive_for(FORWARD, 500, MM)


# Robotu 90° sağa döndür.

drivetrain.turn_for(RIGHT, 90, DEGREES)


# Sürüş ve dönüş hızlarını ayarla.

drivetrain.set_drive_velocity(50, PERCENT)
drivetrain.set_turn_velocity(50, PERCENT)


# Robotun nasıl duracağını belirle.

drivetrain.set_stopping(BRAKE)


# BRAKE → Anında frenler.
# COAST → Yavaşlayarak durur.
# HOLD  → Durduktan sonra tekerlekleri tutar.


# ============================================================
# Ders 01 bitti, bir sonraki derse geçin.
# END OF 01 - DRIVETRAIN BASICS
# ============================================================