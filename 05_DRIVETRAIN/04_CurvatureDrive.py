# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# 04 - CURVATURE DRIVE
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
# CURVATURE DRIVE NEDİR?
# ------------------------------------------------------------
#
# Curvature Drive, Arcade Drive'ın daha kontrollü bir
# versiyonudur.
#
# Arcade Drive'da dönüş miktarı doğrudan motor hızlarına
# eklenir.
#
# Curvature Drive'da ise dönüş etkisi robotun ileri/geri
# hızına bağlıdır.
#
# Böylece robot yüksek hızda daha doğal ve kontrollü
# bir kavis çizerek hareket eder.
#
# Temel olarak:
#
#     forward = ne kadar ilerliyoruz?
#     turn    = ne kadar dönüyoruz?
#
# Dönüşü forward hızına göre ölçeklendiriyoruz.
# ------------------------------------------------------------


while True:
    forward = controller.axis3.position()
    turn = controller.axis4.position()

    turn_effect = turn * abs(forward) / 100

    left_speed = forward + turn_effect
    right_speed = forward - turn_effect

    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)


# ============================================================
# Ders 04 bitti, bir sonraki derse geçin.
# END OF 04 - CURVATURE DRIVE
# ============================================================