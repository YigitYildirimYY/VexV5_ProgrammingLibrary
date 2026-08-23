# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 04 - MOTOR POSITION
# ============================================================

from vex import *


# ============================================================
# POSITION NEDİR?
# ============================================================

# Motor position, motorun encoder'a göre bulunduğu
# açısal konumu ifade eder.
#
# Örneğin:
#
#     0°
#     90°
#     180°
#     360°
#
# gibi değerler kullanılabilir.
#
# Position, motorun "ne kadar hızlı" olduğunu değil,
# "hangi açısal konumda" olduğunu ifade eder.


motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)


# ============================================================
# POSITION OKUMA
# ============================================================

position = motor.position(DEGREES)

print(position)

# Position farklı birimlerle de okunabilir:

position = motor.position(TURNS)

print(position)

# Örneğin:
#
#     360 DEGREES = 1 TURN
#     720 DEGREES = 2 TURNS


# ============================================================
# POSITION SIFIRLAMA
# ============================================================

motor.set_position(0, DEGREES)

# Bundan sonra mevcut konum:
#
#     0°
#
# olarak kabul edilir.
#
# Bu özellikle robotu belirli bir başlangıç pozisyonundan
# kontrol etmek istediğimizde önemlidir.


# ============================================================
# BELİRLİ POZİSYONA GİTME
# ============================================================

motor.set_position(0, DEGREES)

motor.spin_to_position(
    360,
    DEGREES,
    50,
    PERCENT
)

# Motor 360° pozisyonuna gitmeye çalışır.
#
# Burada:
#
#     360       -> hedef pozisyon
#     DEGREES   -> birim
#     50        -> motor hızı
#     PERCENT   -> hız birimi
#
# Position control özellikle:
#
#     Arm
#     Lift
#     Pivot
#
# gibi mekanizmalarda çok kullanışlıdır.


# ============================================================
# POSITION + LIMIT KONTROLÜ
# ============================================================

motor.set_position(0, DEGREES)

motor.spin(FORWARD, 50, PERCENT)

while motor.position(DEGREES) < 360:

    wait(10, MSEC)

motor.stop()

# Burada motoru kendimiz sürekli döndürüyoruz ve
# encoder pozisyonunu kontrol ediyoruz.
#
# 360°'ye ulaştığında:
#
#     motor.stop()
#
# çalışıyor.
#
# Ancak birçok durumda bunun yerine doğrudan:
#
#     spin_to_position()
#
# kullanmak daha temizdir.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Pozisyon oku:
#
#     motor.position(DEGREES)
#
#
# Pozisyonu sıfırla:
#
#     motor.set_position(0, DEGREES)
#
#
# Pozisyona git:
#
#     motor.spin_to_position(
#         360,
#         DEGREES,
#         50,
#         PERCENT
#     )
#
#
# En önemli ayrım:
#
#     velocity()
#         → motor ne kadar hızlı?
#
#     position()
#         → motor nerede?
#
#
# Encoder pozisyonu özellikle autonomous'ta
# mekanizmaların kontrollü hareket ettirilmesi için
# temel bilgilerden biridir.



# ============================================================
# Ders 04 bitti, bir sonraki derse geçin.
# END OF 04 - MOTOR POSITION
# ============================================================