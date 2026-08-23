# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 05 - DERIVATIVE CONTROL
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

imu = Inertial(Ports.PORT7)


# ------------------------------------------------------------
# 1. DERIVATIVE NEDİR?
# ------------------------------------------------------------
#
# P mevcut hataya bakıyordu.
# I geçmişte biriken hataya bakıyordu.
#
# D ise hatanın ne kadar hızlı değiştiğine bakar.
#
# Temel fikir:
#
#     derivative = error - previous_error
#
# Eğer hata çok hızlı azalıyor veya artıyorsa derivative
# bunu fark eder.
#
# Böylece robot hedefe çok hızlı yaklaşırken motor gücünü
# azaltmaya yardımcı olabilir.
# ------------------------------------------------------------


Kp = 0.6
Kd = 0.2

target = 90
previous_error = 0


imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# ------------------------------------------------------------
# 2. P + D KONTROLÜ
# ------------------------------------------------------------
#
# Her döngüde:
#
# 1. Mevcut açıyı okuyoruz.
# 2. Error'u hesaplıyoruz.
# 3. Error'un önceki döngüye göre nasıl değiştiğini buluyoruz.
# 4. P ve D katkılarını birleştiriyoruz.
#
# Formül:
#
#     output = Kp × error + Kd × derivative
# ------------------------------------------------------------

while True:
    current = imu.rotation(DEGREES)
    error = target - current
    derivative = error - previous_error

    output = Kp * error + Kd * derivative

    if output > 100:
        output = 100

    if output < -100:
        output = -100

    if abs(error) <= 1:
        break

    if output > 0:
        left_drive.spin(FORWARD, output, PERCENT)
        right_drive.spin(REVERSE, output, PERCENT)
    else:
        left_drive.spin(REVERSE, abs(output), PERCENT)
        right_drive.spin(FORWARD, abs(output), PERCENT)

    previous_error = error

    wait(20, MSEC)


left_drive.stop(BRAKE)
right_drive.stop(BRAKE)


# ------------------------------------------------------------
# 3. D NEYİ DEĞİŞTİRİYOR?
# ------------------------------------------------------------
#
# Diyelim robot hedefe çok hızlı yaklaşıyor:
#
#     Error:
#     20 → 10 → 5 → 2
#
# Error sürekli hızlı şekilde azalıyor.
#
# D bunu fark edip çıkışa karşı koymaya başlar.
#
# Bu nedenle D özellikle overshoot'u ve salınımı azaltmaya
# yardımcı olur.
#
# Fakat D çok yüksek olursa sensördeki küçük değişikliklere
# bile fazla tepki verebilir. Bu yüzden özellikle sensör
# gürültüsü olan sistemlerde dikkatli ayarlanır.
# ------------------------------------------------------------


# ============================================================
# Ders 05 bitti, bir sonraki derse geçin.
# END OF 05 - DERIVATIVE CONTROL
# ============================================================