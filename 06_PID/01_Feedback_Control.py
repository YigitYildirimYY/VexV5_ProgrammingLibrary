# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 01 - FEEDBACK CONTROL
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
# FEEDBACK CONTROL NEDİR?
# ------------------------------------------------------------
#
# Bir robotu kontrol etmenin iki temel yolu vardır.
#
# Open-loop kontrolde robotun gerçekten ne yaptığını
# kontrol etmeyiz.
#
# Örneğin:
#
#     Motorları çalıştır
#     1 saniye bekle
#     Motorları durdur
#
# Robotun gerçekten ne kadar döndüğünü bilmiyoruz.
#
# Feedback control'de ise sensör robotun gerçek durumunu
# sürekli ölçer ve bu bilgiye göre karar verir.
#
# Örneğin:
#
#     "90° dön."
#
# Robot dönerken IMU'yu sürekli okuruz ve gerçekten kaç
# derece döndüğünü kontrol ederiz.
# ------------------------------------------------------------


target = 90


# IMU kalibrasyonu sırasında robot hareketsiz olmalıdır.

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# ------------------------------------------------------------
# FEEDBACK LOOP
# ------------------------------------------------------------
#
# Robotu sabit bir hızla döndürüyoruz, fakat ne zaman
# duracağını sensörden gelen bilgi belirliyor.
#
# Bu henüz PID değildir.
# Sadece feedback control mantığını gösteriyoruz.
# ------------------------------------------------------------

left_drive.spin(FORWARD, 30, PERCENT)
right_drive.spin(REVERSE, 30, PERCENT)

while True:
    current = imu.rotation(DEGREES)

    if current >= target:
        break

    wait(10, MSEC)


left_drive.stop(BRAKE)
right_drive.stop(BRAKE)


# ------------------------------------------------------------
# NEDEN FEEDBACK DAHA İYİ?
# ------------------------------------------------------------
#
# Open-loop:
#
#     "30% güçte 1 saniye çalış."
#
# Bu yöntemde robotun gerçekten kaç derece döndüğünü
# bilmiyoruz.
#
# Feedback:
#
#     "30% güçte dön ve IMU'yu sürekli kontrol et."
#
# Robot 90°'ye ulaştığında duruyor.
#
# Böylece robotun gerçek hareketini kontrol sistemine
# dahil etmiş oluyoruz.
#
# PID'nin yaptığı şey de bu feedback mantığını çok daha
# akıllı hale getirmektir.
#
# PID yalnızca:
#
#     "90° oldu mu?"
#
# diye bakmak yerine, hedefe ne kadar uzak olduğumuzu,
# geçmişteki hatayı ve hatanın ne kadar hızlı değiştiğini
# kullanarak motor gücünü sürekli ayarlar.


# ============================================================
# Ders 01 bitti, bir sonraki derse geçin.
# END OF 01 - FEEDBACK CONTROL
# ============================================================