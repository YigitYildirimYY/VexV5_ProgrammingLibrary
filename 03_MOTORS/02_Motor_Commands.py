# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 02 - MOTOR COMMANDS
# ============================================================

from vex import *


# ============================================================
# MOTOR
# ============================================================

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)


# ============================================================
# SPIN
# ============================================================

# spin() motoru sürekli döndürür.
#
# Temel kullanım:

motor.spin(FORWARD)

# Motor, stop() komutu verilene kadar dönmeye devam eder.
#
# Yön:
#
#     FORWARD
#     REVERSE
#
# Örneğin:

motor.spin(REVERSE)


# ============================================================
# SPIN + HIZ
# ============================================================

# Motorun hızını doğrudan spin() içinde verebiliriz.

motor.spin(
    FORWARD,
    50,
    PERCENT
)

# Burada:
#
#     FORWARD -> yön
#     50       -> hız
#     PERCENT  -> hız birimi
#
# Aynı şekilde:

motor.spin(
    FORWARD,
    120,
    RPM
)

# Burada hız RPM cinsindendir.
#
# Kullanabileceğimiz temel velocity units:
#
#     PERCENT
#     RPM
#     VOLT
#
# Ancak VOLT motorun hızını değil, motora uygulanan
# gerilimi belirler.


# ============================================================
# SET VELOCITY + SPIN
# ============================================================

# Hızı önceden de belirleyebiliriz.

motor.set_velocity(50, PERCENT)

motor.spin(FORWARD)

# Bu durumda spin() sırasında ayrıca hız belirtmezsek
# daha önce ayarlanan velocity kullanılır.
#
# Örneğin:

motor.set_velocity(100, PERCENT)

motor.spin(FORWARD)

wait(1, SECONDS)

motor.stop()


# ============================================================
# STOP
# ============================================================

# Motoru durdurmak için stop() kullanılır.

motor.stop()

# stop() tek başına kullanıldığında motorun mevcut
# braking ayarına göre durmasını sağlar.
#
# Fren davranışını ileride:
#
#     08_Motor_Braking.py
#
# dosyasında inceleyeceğiz.


# ============================================================
# SPIN FOR
# ============================================================

# spin_for(), motoru belirli bir miktar döndürür.
#
# Örneğin:

motor.spin_for(
    FORWARD,
    360,
    DEGREES
)

# Bu komut motoru 360 derece döndürür.
#
# Başka bir örnek:

motor.spin_for(
    FORWARD,
    2,
    TURNS
)

# Motor 2 tur döner ve ardından komut tamamlanır.
#
# Bu komut autonomous'ta özellikle kullanışlıdır.
#
# spin():
#
#     Sürekli döner.
#
# spin_for():
#
#     Belirlenen miktar kadar döner.


# ============================================================
# ÖNEMLİ: WAIT GEREKMEYEBİLİR
# ============================================================

# spin_for() tamamlanana kadar kod normalde bekler.

motor.spin_for(
    FORWARD,
    720,
    DEGREES
)

print("Motor movement finished")

# Burada motor hareketini tamamladıktan sonra
# print() çalışır.
#
# Bu nedenle sadece motorun belirli bir miktar dönmesini
# istiyorsak ayrıca:
#
#     wait(...)
#
# kullanmak zorunda değiliz.


# ============================================================
# SPIN TO POSITION
# ============================================================

# Motorun belirli bir encoder pozisyonuna gitmesini
# sağlayabiliriz.

motor.set_position(0, DEGREES)

motor.spin_to_position(
    360,
    DEGREES,
    50,
    PERCENT
)

# Burada motorun pozisyonunu önce sıfırladık.
#
# Daha sonra:
#
#     360 derece
#
# pozisyonuna gitmesini istedik.
#
# spin_for() ile spin_to_position() arasındaki temel fark:
#
# spin_for():
#     "Şu kadar dön."
#
# spin_to_position():
#     "Şu pozisyona git."
#
# Pozisyon kontrolünü daha ayrıntılı olarak:
#
#     04_Motor_Position.py
#
# dosyasında inceleyeceğiz.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Sürekli döndür:
#
#     motor.spin(FORWARD)
#
#
# Belirli hızla döndür:
#
#     motor.spin(FORWARD, 50, PERCENT)
#
#
# Hızı önceden belirle:
#
#     motor.set_velocity(50, PERCENT)
#
#
# Durdur:
#
#     motor.stop()
#
#
# Belirli miktar döndür:
#
#     motor.spin_for(FORWARD, 360, DEGREES)
#
#
# Belirli pozisyona git:
#
#     motor.spin_to_position(360, DEGREES, 50, PERCENT)
#
#
# En önemli ayrım:
#
#     spin()
#         → sürekli hareket
#
#     spin_for()
#         → belirli miktar hareket
#
#     spin_to_position()
#         → belirli encoder pozisyonuna git



# ============================================================
# Ders 02 bitti, bir sonraki derse geçin.
# END OF 02 - MOTOR COMMANDS
# ============================================================