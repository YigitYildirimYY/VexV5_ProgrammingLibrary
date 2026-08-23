# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 07 - PID TUNING
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
# PID TUNING NEDİR?
# ------------------------------------------------------------
#
# Kp, Ki ve Kd değerleri robotun davranışını belirler.
# Bu değerleri tek seferde bulmak yerine kontrollü şekilde
# değiştirip robotun tepkisini gözlemleyerek ayarlarız.
#
# Genel yaklaşım:
#
# 1. Ki ve Kd'yi 0 yap.
# 2. Kp'yi artırarak uygun tepkiyi bul.
# 3. Fazla overshoot varsa Kd ekle.
# 4. Hedefte sürekli hata kalıyorsa Ki ekle.
#
# Her seferinde mümkün olduğunca tek bir değeri değiştirmek,
# hangi parametrenin ne yaptığını anlamayı kolaylaştırır.
# ------------------------------------------------------------

Kp = 0.6
Ki = 0.0
Kd = 0.2

target = 90

integral = 0
previous_error = 0

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# ------------------------------------------------------------
# PID TESTİ
# ------------------------------------------------------------
#
# Bu döngü sırasında robotun davranışını gözlemleyebiliriz.
#
# Önemli şeyler:
#
# - Hedefe ne kadar hızlı ulaşıyor?
# - Hedefi geçiyor mu?
# - Hedef çevresinde sallanıyor mu?
# - Hedefe ulaştığında küçük bir hata kalıyor mu?
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
# TUNING YAPARKEN NEYE BAKILIR?
# ------------------------------------------------------------
#
# Kp çok düşük:
# Robot hedefe yavaş yaklaşır ve tepkisi zayıf kalır.
#
# Kp çok yüksek:
# Robot hedefi geçebilir ve ileri-geri sallanabilir.
#
# Kd düşükse:
# Overshoot ve salınım daha belirgin olabilir.
#
# Kd çok yüksekse:
# Sistem fazla yavaşlayabilir ve sensör gürültüsüne
# gereğinden fazla tepki verebilir.
#
# Ki düşükse:
# Hedefte küçük bir kalıcı hata kalabilir.
#
# Ki çok yüksekse:
# Integral fazla birikir ve sistem salınmaya başlayabilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# ÖRNEK TUNING SÜRECİ
# ------------------------------------------------------------
#
# Önce:
#
#     Kp = 0.5
#     Ki = 0
#     Kd = 0
#
# Robotun tepkisini gözlemleriz.
#
# Daha hızlı tepki gerekiyorsa Kp'yi artırırız.
#
# Örneğin:
#
#     0.5 → 0.6 → 0.7
#
# Robot belirgin şekilde overshoot yapmaya başladığında
# Kp'yi biraz geri çekeriz veya Kd ekleriz.
#
# Daha sonra küçük bir Ki değeri deneyerek hedefte kalan
# hatayı azaltabiliriz.
# ------------------------------------------------------------


# ============================================================
# Ders 07 bitti, bir sonraki derse geçin.
# END OF 07 - PID TUNING
# ============================================================