# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 11 - PID DEBUGGING
# ============================================================


# Bu bölümde PID ile çalışırken karşılaştığımız sorunlara (BUG) nasıl çözümler üretmemiz gerektiğini öğreneceğiz.
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
# PID DEBUGGING
# ------------------------------------------------------------
#
# PID çalışmadığında doğrudan Kp, Ki ve Kd ile oynamak yerine
# önce robotun ne yaptığını görmeliyiz.
#
# En faydalı değerler:
#
# current     → robot şu anda nerede?
# error       → hedeften ne kadar uzakta?
# integral    → hata ne kadar birikti?
# derivative  → hata ne kadar hızlı değişiyor?
# output      → PID motorlara ne kadar güç veriyor?
#
# Bu değerleri Brain ekranında görmek tuning'i çok daha
# kolaylaştırır.
# ------------------------------------------------------------


Kp = 0.6
Ki = 0.01
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

    brain.screen.clear_screen()

    brain.screen.print("Current: ", current)
    brain.screen.next_row()
    brain.screen.print("Error: ", error)
    brain.screen.next_row()
    brain.screen.print("Integral: ", integral)
    brain.screen.next_row()
    brain.screen.print("Derivative: ", derivative)
    brain.screen.next_row()
    brain.screen.print("Output: ", output)

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
# PID SORUNUNU NASIL ANLARIZ?
# ------------------------------------------------------------
#
# Robot çok yavaşsa:
#     Kp düşük olabilir.
#
# Robot hedefi geçip sallanıyorsa:
#     Kp fazla veya Kd yetersiz olabilir.
#
# Robot hedefe yaklaşıp biraz uzakta kalıyorsa:
#     Ki yetersiz olabilir.
#
# Integral çok hızlı büyüyorsa:
#     Ki fazla olabilir veya integral sınırlandırılmalıdır.
#
# Output sürekli 100'e dayanıyorsa:
#     PID kontrolü çıkış sınırına takılıyor olabilir.
#
# Değerler çok oynuyorsa:
#     Sensör gürültüsü veya fazla yüksek Kd söz konusu olabilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# DEBUGGING ALIŞKANLIĞI
# ------------------------------------------------------------
#
# Önce sensörü kontrol et.
# Sonra error'u kontrol et.
# Sonra PID çıktısına bak.
# En son Kp, Ki ve Kd'yi değiştir.
#
# Böylece "robot kötü çalışıyor" demek yerine problemin
# hangi aşamada olduğunu bulabiliriz.
# ------------------------------------------------------------


# ============================================================
# Ders 11 bitti, bir sonraki derse geçin.
# END OF 11 - PID DEBUGGING
# ============================================================