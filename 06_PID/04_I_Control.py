# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 04 - INTEGRAL CONTROL
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
# 1. INTEGRAL NEDİR?
# ------------------------------------------------------------
#
# P sadece mevcut hataya bakıyordu:
#
#     output = Kp × error
#
# Integral ise geçmiş hataları biriktirir.
#
# Bunun temel mantığı:
#
#     integral += error
#
# Böylece küçük bir hata uzun süre devam ediyorsa
# integral giderek büyür ve sistemi hedefe doğru
# biraz daha fazla iter.
#
# Örneğin hata sürekli 2° ise:
#
#     2 → 4 → 6 → 8 → ...
#
# Integral şunu fark eder:
#
#     "Hata küçük ama sürekli devam ediyor."
# ------------------------------------------------------------


Kp = 0.6
Ki = 0.01
target = 90

integral = 0


# IMU kalibrasyonu sırasında robot hareketsiz olmalıdır.

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# ------------------------------------------------------------
# 2. P + I KONTROLÜ
# ------------------------------------------------------------
#
# Her döngüde:
#
# 1. Mevcut açıyı okuyoruz.
# 2. Error'u hesaplıyoruz.
# 3. Error'u integral'e ekliyoruz.
# 4. P ve I katkılarını topluyoruz.
#
# Formül:
#
#     output = Kp × error + Ki × integral
# ------------------------------------------------------------

while True:
    current = imu.rotation(DEGREES)
    error = target - current

    integral += error

    output = Kp * error + Ki * integral

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

    wait(20, MSEC)


left_drive.stop(BRAKE)
right_drive.stop(BRAKE)


# ------------------------------------------------------------
# 3. INTEGRAL'IN FAYDASI
# ------------------------------------------------------------
#
# Diyelim ki robot 88° civarında kalıyor.
#
# Error:
#
#     90 - 88 = 2°
#
# P'nin katkısı:
#
#     Kp × 2
#
# çok küçük olabilir.
#
# Ama bu 2° hata sürekli devam ederse integral büyür ve
# ekstra çıkış oluşturarak robotun hedefe yaklaşmasına
# yardımcı olur.
#
# Integral fazla büyürse bu sefer sistem hedefi aşabilir.
# Buna integral windup denir.
#
# Bu yüzden gerçek PID sistemlerinde integral genellikle
# bir sınır içinde tutulur.
# ------------------------------------------------------------


# ============================================================
# Ders 04 bitti, bir sonraki derse geçin.
# END OF 04 - INTEGRAL CONTROL
# ============================================================