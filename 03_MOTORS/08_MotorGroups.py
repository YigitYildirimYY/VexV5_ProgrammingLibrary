# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 09 - MOTOR GROUPS
# ============================================================

from vex import *


brain = Brain()


# ============================================================
# 01 - MOTOR GROUP NEDİR?
# ============================================================

# MotorGroup, birden fazla motoru tek bir nesne
# üzerinden birlikte kontrol etmemizi sağlar.
#
# Örneğin bir lift için:
#
#     motor_1
#     motor_2
#
# yerine:
#
#     lift
#
# isimli tek bir MotorGroup kullanabiliriz.


motor_1 = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

motor_2 = Motor(
    Ports.PORT2,
    GearSetting.RATIO_18_1,
    False
)

lift = MotorGroup(
    motor_1,
    motor_2
)


# ============================================================
# 02 - MOTOR GROUP İLE MOTORLARI ÇALIŞTIRMA
# ============================================================

lift.spin(
    FORWARD,
    50,
    PERCENT
)

wait(1, SECONDS)

lift.stop()

# lift üzerinden verilen komut iki motor için de
# uygulanır.


# ============================================================
# 03 - MOTOR GROUP İLE SPIN_FOR
# ============================================================

lift.spin_for(
    FORWARD,
    360,
    DEGREES
)

# Grup içerisindeki motorlar birlikte 360 derece
# hareket eder.


# ============================================================
# 04 - MOTOR GROUP AYARLARI
# ============================================================

lift.set_velocity(
    50,
    PERCENT
)

lift.spin(FORWARD)

wait(1, SECONDS)

lift.stop()

# MotorGroup, Motor'daki birçok hareket ve ayar
# metodunu birlikte kullanabilir.


# ============================================================
# 05 - MOTOR SAYISINI ÖĞRENME
# ============================================================

motor_count = lift.count()

brain.screen.clear_screen()
brain.screen.print(f"Motors: {motor_count}")

# count() yalnızca MotorGroup için kullanılır.
#
# Bu örnekte:
#
#     motor_count = 2
#
# olur.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# MotorGroup oluştur:
#
#     lift = MotorGroup(
#         motor_1,
#         motor_2
#     )
#
#
# Birlikte çalıştır:
#
#     lift.spin(FORWARD, 50, PERCENT)
#
#
# Durdur:
#
#     lift.stop()
#
#
# Motor sayısını öğren:
#
#     lift.count()
#
#
# MotorGroup özellikle:
#
#     Drivetrain
#     Lift
#     Arm
#     Intake
#
# gibi birden fazla motorun birlikte çalıştığı
# mekanizmalarda kullanışlıdır.
#
# Önemli:
#
# MotorGroup içindeki motorları tek tek de
# kontrol edebiliriz:
#
#     motor_1.spin(...)
#     motor_2.spin(...)
#
# ancak ortak hareketler için MotorGroup kullanmak
# kodu daha temiz hale getirir.


# ============================================================
# Ders 09 bitti, bir sonraki derse geçin.
# END OF 09 - MOTOR GROUPS
# ============================================================


"""
BU DERSLE BERABER MOTORS KONUSU BİTTİ.

Sıradaki konu;
SENSORS

"""