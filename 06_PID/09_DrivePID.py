# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 09 - DRIVE PID
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

tracking = Rotation(Ports.PORT7)


# ------------------------------------------------------------
# DRIVE PID NEDİR?
# ------------------------------------------------------------
#
# Turn PID'de:
#
#     Hedef = belirli bir açı
#
# Drive PID'de:
#
#     Hedef = belirli bir mesafe
#
# Rotation Sensor tracking wheel'in ne kadar döndüğünü
# ölçüyor. Tekerleğin çevresini bildiğimiz için bunu
# mesafeye çevirebiliriz.
#
# Sonra PID:
#
#     Hedef mesafe - Gerçek mesafe
#
# hatasına göre motor gücünü ayarlar.
# ------------------------------------------------------------

Kp = 0.5
Ki = 0.01
Kd = 0.2

target_distance = 1000

wheel_diameter = 50
wheel_circumference = wheel_diameter * 3.14159

integral = 0
previous_error = 0


# Tracking wheel'in mevcut konumunu başlangıç olarak sıfırlarız.

tracking.reset_position()


# ------------------------------------------------------------
# DRIVE PID DÖNGÜSÜ
# ------------------------------------------------------------

while True:
    wheel_turns = tracking.position(TURNS)

    current_distance = wheel_turns * wheel_circumference

    error = target_distance - current_distance

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
# Hedefimiz 1000 mm olsun.
#
# Tracking wheel:
#
#     "Şu ana kadar 600 mm gittin."
#
# PID:
#
#     error = 1000 - 600
#           = 400 mm
#
# Hata büyük olduğu için daha fazla güç verir.
#
# Robot ilerledikçe:
#
#     600 → 800 → 930 → 985 → 1000 mm
#
# hata küçülür ve motor gücü azalır.
#
# Böylece robot sadece "motorları 2 saniye çalıştır"
# demek yerine gerçekten ne kadar yol aldığını ölçerek
# hareketini düzeltir.
# ------------------------------------------------------------


# ============================================================
# Ders 09 bitti, bir sonraki derse geçin.
# END OF 09 - DRIVE PID
# ============================================================