# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 10 - DISTANCE PID
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

distance = Distance(Ports.PORT7)


# ------------------------------------------------------------
# DISTANCE PID NEDİR?
# ------------------------------------------------------------
#
# Bu kez hedefimiz bir açı veya gidilecek mesafe değil,
# Distance Sensor ile ölçülen belirli bir uzaklık.
#
# Örneğin:
#
# target = 300 mm
#
# Sensör 450 mm okuyorsa robot fazla uzaktadır.
# Sensör 320 mm okuyorsa yine biraz uzaktadır.
# Sensör 300 mm okuyorsa hedefe ulaşılmıştır.
#
# PID sürekli:
#
#     error = target - current
#
# hesabını yaparak motor gücünü ayarlar.
# ------------------------------------------------------------

Kp = 0.4
Ki = 0.01
Kd = 0.2

target = 300

integral = 0
previous_error = 0


# ------------------------------------------------------------
# DISTANCE PID DÖNGÜSÜ
# ------------------------------------------------------------

while True:
    current = distance.object_distance(MM)

    error = target - current

    integral += error
    derivative = error - previous_error

    output = Kp * error + Ki * integral + Kd * derivative

    if output > 100:
        output = 100

    if output < -100:
        output = -100

    if abs(error) <= 5:
        break

    if output > 0:
        left_drive.spin(FORWARD, output, PERCENT)
        right_drive.spin(FORWARD, output, PERCENT)
    else:
        left_drive.spin(REVERSE, abs(output), PERCENT)
        right_drive.spin(REVERSE, abs(output), PERCENT)

    previous_error = error

    wait(20, MSEC)


left_drive.stop(BRAKE)
right_drive.stop(BRAKE)


# ------------------------------------------------------------
# NASIL ÇALIŞIYOR?
# ------------------------------------------------------------
#
# Hedefimiz 300 mm olsun.
#
# Sensör 500 mm okursa:
#
#     error = 300 - 500
#           = -200 mm
#
# Robot hedefe uzakta olduğu için ileri doğru hareket eder.
#
# Sensör 350 mm okuduğunda hata küçülür ve PID daha az
# güç verir.
#
# Sensör 303 mm olduğunda hata çok küçüktür ve robot
# yavaşlar.
#
# 300 mm civarına geldiğinde toleransın içine girip durur.
# ------------------------------------------------------------


# ============================================================
# Ders 10 bitti, bir sonraki derse geçin.
# END OF 10 - DISTANCE PID
# ============================================================