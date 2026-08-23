# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 03 - MOTOR VELOCITY
# ============================================================

from vex import *


# ============================================================
# VELOCITY NEDİR?
# ============================================================

# Velocity, motorun ne kadar hızlı dönmesini belirler.
#
# VEX'te en sık:
#
#     PERCENT
#     RPM
#
# kullanılır.
#
# Örneğin:

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

motor.set_velocity(50, PERCENT)

motor.spin(FORWARD)

wait(1, SECONDS)

motor.stop()


# ============================================================
# SET VELOCITY
# ============================================================

# Hızı önceden ayarlayabiliriz:

motor.set_velocity(80, PERCENT)

motor.spin(FORWARD)

# Bundan sonra hız belirtilmeyen motor komutlarında
# ayarlanan velocity kullanılabilir.


# ============================================================
# KOMUT İÇİNDE HIZ BELİRLEME
# ============================================================

# Hızı doğrudan spin() içinde de verebiliriz:

motor.spin(
    FORWARD,
    60,
    PERCENT
)

# Bu kullanımda verilen hız o komut için kullanılır.


# ============================================================
# VELOCITY OKUMA
# ============================================================

motor.set_velocity(70, PERCENT)

velocity = motor.velocity(PERCENT)

print(velocity)

# velocity() motorun mevcut velocity ayarını okumak
# için kullanılabilir.
#
# Örneğin RPM olarak:

rpm = motor.velocity(RPM)

print(rpm)


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Hız ayarla:
#
#     motor.set_velocity(50, PERCENT)
#
# Hız ile çalıştır:
#
#     motor.spin(FORWARD, 50, PERCENT)
#
# Hızı oku:
#
#     motor.velocity(PERCENT)
#
# veya:
#
#     motor.velocity(RPM)
#
# PERCENT:
#     Yüzde üzerinden hız.
#
# RPM:
#     Dakikadaki dönüş sayısı.
#
# Önemli:
# set_velocity() motoru çalıştırmaz.
# Sadece sonraki hareket komutlarında kullanılacak
# hızı belirler.



# ============================================================
# Ders 03 bitti, bir sonraki derse geçin.
# END OF 03 - MOTOR VELOCITY
# ============================================================