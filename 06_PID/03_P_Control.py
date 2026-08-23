# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 03 - P CONTROL
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
# P CONTROL NEDİR?
# ------------------------------------------------------------
#
# P (Proportional), motor gücünü mevcut hataya göre belirler.
#
# Hata büyükse daha güçlü müdahale ederiz.
# Hata küçüldükçe motor gücü de azalır.
#
# Formül:
#
#     output = Kp × error
#
# Kp, P'nin ne kadar güçlü tepki vereceğini belirler.
# ------------------------------------------------------------

Kp = 0.6
target = 90


imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# ------------------------------------------------------------
# P KONTROL DÖNGÜSÜ
# ------------------------------------------------------------
#
# Her döngüde:
#
# 1. Robotun mevcut açısını okuyoruz.
# 2. Hedef ile arasındaki hatayı buluyoruz.
# 3. Hata × Kp ile motor gücünü hesaplıyoruz.
# 4. Robotu bu güçle döndürüyoruz.
# 5. Biraz sonra tekrar ölçüyoruz.
#
# Böylece robot hedefe yaklaştıkça verdiğimiz güç azalıyor.
# ------------------------------------------------------------

while True:
    current = imu.rotation(DEGREES)
    error = target - current
    output = Kp * error

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
# P'NİN DAVRANIŞI
# ------------------------------------------------------------
#
# Örneğin hedefimiz 90° ve Kp = 0.6 olsun:
#
# 30° → error = 60° → output = 36%
# 60° → error = 30° → output = 18%
# 80° → error = 10° → output =  6%
# 89° → error =  1° → output =  0.6%
#
# Yani robot hedefe yaklaştıkça yavaşlıyor.
#
# P'nin problemi ise şu:
# Hedefe çok yaklaştığında output çok küçülebilir ve robot
# 90°'ye tam ulaşmadan durabilir.
#
# Bu yüzden sadece P her zaman yeterli değildir.
# ------------------------------------------------------------


# ============================================================
# Ders 03 bitti, bir sonraki derse geçin.
# END OF 03 - P CONTROL
# ============================================================