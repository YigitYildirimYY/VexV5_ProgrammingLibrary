# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 08 - TURN PID
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
# TURN PID
# ------------------------------------------------------------
#
# Hedefimiz robotu tam 90° döndürmek.
#
# IMU robotun gerçek dönüşünü ölçüyor.
# PID ise bu ölçüme göre motor gücünü sürekli ayarlıyor.
#
# Kp → mevcut hataya tepki
# Ki → biriken hatayı düzeltme
# Kd → hatanın değişim hızına tepki
# ------------------------------------------------------------

Kp = 0.6
Ki = 0.01
Kd = 0.2

target = 90

integral = 0
previous_error = 0


# ------------------------------------------------------------
# IMU KALİBRASYONU
# ------------------------------------------------------------

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# ------------------------------------------------------------
# TURN PID DÖNGÜSÜ
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
# NASIL ÇALIŞIYOR?
# ------------------------------------------------------------
#
# Örneğin robot 0°'de başlıyor ve hedefimiz 90°.
#
# 0°  → error = 90°
# 30° → error = 60°
# 60° → error = 30°
# 80° → error = 10°
#
# Robot hedefe yaklaştıkça P çıkışı azalıyor.
# I, sürekli kalan küçük hataları düzeltmeye yardım ediyor.
# D ise robot hedefe çok hızlı yaklaşırken sistemi sakinleştiriyor.
#
# Sonuç olarak motor gücü sabit değil;
# robotun gerçek hareketine göre sürekli değişiyor.
# ------------------------------------------------------------


# ============================================================
# Ders 08 bitti, bir sonraki derse geçin.
# END OF 08 - TURN PID
# ============================================================