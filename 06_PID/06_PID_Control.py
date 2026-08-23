# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 06 - PID CONTROL
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
# PID NEDİR?
# ------------------------------------------------------------
#
# PID, robotun gerçek durumunu sürekli ölçüp hedefle
# karşılaştırarak motor gücünü buna göre ayarlayan bir
# feedback control yöntemidir.
#
# P → Şu anda ne kadar hatamız var?
# I → Bu hata ne kadar birikti?
# D → Hata ne kadar hızlı değişiyor?
#
# Formül:
#
# output = Kp × error
#        + Ki × integral
#        + Kd × derivative
# ------------------------------------------------------------


Kp = 0.6
Ki = 0.01
Kd = 0.2

target = 90

integral = 0
previous_error = 0


# IMU kalibrasyonu sırasında robot hareketsiz olmalıdır.

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# ------------------------------------------------------------
# PID DÖNGÜSÜ
# ------------------------------------------------------------
#
# Her döngüde robotun gerçek açısını okuyoruz.
# Sonra hata, integral ve derivative hesaplanıyor.
#
# Bu üç bilgi birleşerek motor çıktısını oluşturuyor.
# ------------------------------------------------------------

while True:
    current = imu.rotation(DEGREES)

    error = target - current

    integral += error

    derivative = error - previous_error

    output = Kp * error + Ki * integral + Kd * derivative

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
# PID'NİN HER PARÇASI NE YAPIYOR?
# ------------------------------------------------------------
#
# P:
# Hata büyükse güçlü, küçükse daha yumuşak tepki verir.
#
# I:
# Küçük ama sürekli devam eden hataları zaman içinde
# düzeltmeye yardımcı olur.
#
# D:
# Hata hızlı değişiyorsa buna tepki vererek overshoot ve
# salınımı azaltmaya yardımcı olur.
#
# Üçü birlikte robotun hedefe daha hızlı, daha hassas ve
# daha kontrollü ulaşmasını sağlar.
# ------------------------------------------------------------


# ============================================================
# Ders 06 bitti, bir sonraki derse geçin.
# END OF 06 - PID CONTROL
# ============================================================