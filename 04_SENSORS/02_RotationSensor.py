# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 02 - ROTATION SENSOR
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. ROTATION SENSOR NEDİR?
# ------------------------------------------------------------
#
# Rotation Sensor, bağlı olduğu bir milin (shaft) dönüşünü
# ölçer.
#
# Örneğin bir tracking wheel'e bağlanırsa:
#
#        Tracking Wheel
#              
#       Rotation Sensor
#              
#       "Ne kadar döndü?"
#
# Rotation Sensor:
# - Açıyı ölçebilir.
# - Toplam pozisyonu ölçebilir.
# - Dönüş hızını ölçebilir.
#
# Motorların kendi encoder'ları vardır.
# Rotation Sensor ise ayrı bir shaft'ın dönüşünü
# harici bir encoder gibi takip edebilir.
#
# Özellikle:
# - Odometry
# - Tracking wheels
# - Mekanizma pozisyonu
# - Hassas hareket kontrolü
# için kullanılır.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. SENSOR TANIMLAMA
# ------------------------------------------------------------

brain = Brain()

rotation = Rotation(Ports.PORT7)


# ------------------------------------------------------------
# 3. ANGLE
# ------------------------------------------------------------
#
# angle(), shaft'ın mevcut açısını verir.
#
# Değer 0° ile 359.99° arasındadır.
#
# Örneğin:
#
# 0°   → başlangıç
# 90°  → çeyrek tur
# 180° → yarım tur
# 270° → üç çeyrek tur
#
# 360° olduğunda tekrar 0° civarına gelir.
#
# IMPORTANT:
# angle() toplam kaç derece dönüldüğünü göstermez.
# Sadece mevcut turun içindeki açıyı gösterir.
# ------------------------------------------------------------

angle = rotation.angle(DEGREES)

brain.screen.print("Angle:", angle)


# ------------------------------------------------------------
# 4. POSITION
# ------------------------------------------------------------
#
# position(), shaft'ın proje boyunca toplam ne kadar
# döndüğünü gösterir.
#
# angle() ile arasındaki en önemli fark:
#
# angle():
#     0° - 359.99°
#
# position():
#     360°'yi geçebilir.
#     0°'nin altına da inebilir.
#
# Örneğin:
#
# 1 tur  → 360°
# 2 tur  → 720°
# 3 tur  → 1080°
#
# Ters yönde dönerse:
#
# -360°
# -720°
# ...
# ------------------------------------------------------------

position = rotation.position(DEGREES)

brain.screen.print("Position:", position)


# ------------------------------------------------------------
# 5. POSITION IN TURNS
# ------------------------------------------------------------
#
# Position değerini turns olarak da okuyabiliriz.
#
# 1 turn = 360°
#
# Örneğin:
#
# 720° = 2 turns
# ------------------------------------------------------------

turns = rotation.position(TURNS)

brain.screen.print("Turns:", turns)


# ------------------------------------------------------------
# 6. SET_POSITION
# ------------------------------------------------------------
#
# set_position(), sensörün mevcut position değerini
# istediğimiz bir değere ayarlar.
#
# IMPORTANT:
# Bu komut fiziksel olarak sensörü döndürmez.
#
# Sadece programın sensörden okuyacağı position değerini
# değiştirir.
# ------------------------------------------------------------

rotation.set_position(0, DEGREES)


# Artık sensörün position değeri:
#
# 0°
#
# kabul edilir.


# ------------------------------------------------------------
# 7. RESET_POSITION
# ------------------------------------------------------------
#
# reset_position(), position değerini doğrudan 0'a sıfırlar.
#
# Örneğin:
#
# rotation.reset_position()
#
# sonrasında:
#
# position = 0°
#
# olur.
# ------------------------------------------------------------

rotation.reset_position()


# ------------------------------------------------------------
# 8. VELOCITY
# ------------------------------------------------------------
#
# velocity(), shaft'ın dönme hızını verir.
#
# VEX V5 Python API'de iki birim kullanılabilir:
#
# RPM → Revolutions Per Minute
# DPS → Degrees Per Second
#
# Örneğin:
#
# 60 RPM
# → dakikada 60 tur
#
# 180 DPS
# → saniyede 180 derece
# ------------------------------------------------------------

velocity_rpm = rotation.velocity(RPM)

brain.screen.print("Velocity RPM:", velocity_rpm)


velocity_dps = rotation.velocity(DPS)

brain.screen.print("Velocity DPS:", velocity_dps)


# ------------------------------------------------------------
# 9. SET_REVERSED
# ------------------------------------------------------------
#
# Sensörün yönünü ters çevirmek için kullanılır.
#
# Eğer sensörün fiziksel yönü nedeniyle:
#
# İleri dönüş = negatif
#
# olarak okunuyorsa:
#
# rotation.set_reversed(True)
#
# kullanabiliriz.
#
# Böylece pozitif ve negatif değerlerin yönü tersine çevrilir.
# ------------------------------------------------------------

rotation.set_reversed(False)


# ------------------------------------------------------------
# 10. BASİT BİR HAREKET ÖLÇÜMÜ
# ------------------------------------------------------------
#
# Sensörün position değerini sıfırlayalım.
# ------------------------------------------------------------

rotation.reset_position()


# Daha sonra bir mekanizma veya tracking wheel hareket
# ettiğinde position değerini okuyabiliriz:

current_position = rotation.position(DEGREES)

brain.screen.print("Position:", current_position)


# ------------------------------------------------------------
# 11. 2 TUR DÖNÜŞÜ ALGILAMAK
# ------------------------------------------------------------
#
# Burada Rotation Sensor'ın kendisini döndürmüyoruz.
#
# Sensorun bağlı olduğu shaft'ın başka bir sistem tarafından
# döndürülmesini bekliyoruz.
#
# 2 tur = 720°
# ------------------------------------------------------------

rotation.reset_position()

while rotation.position(DEGREES) < 720:
    wait(10, MSEC)


# Buraya geldiğimizde shaft en az 720° dönmüştür.
#
# ÖNEMLİ:
# Bu kod motorları çalıştırmaz.
# Sadece sensörün ölçtüğü değeri kontrol eder.


# ------------------------------------------------------------
# 12. TRACKING WHEEL İLE MESAFE
# ------------------------------------------------------------
#
# Rotation Sensor bir tracking wheel'e bağlanırsa,
# tekerleğin dönüşünden alınan mesafe hesaplanabilir.
#
# Örneğin:
#
# Wheel diameter = 100 mm
#
# Circumference:
#
#     π × 100 ≈ 314.16 mm
#
# 1 tur:
#     ≈ 314.16 mm
#
# 2 tur:
#     ≈ 628.32 mm
#
# Böylece:
# Alınan mesafe hesaplanabilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 13. ODOMETRY İLE BAĞLANTISI
# ------------------------------------------------------------
#
# Rotation Sensor, özellikle tracking wheel'lerde
# odometry için kullanılabilir.
#
# Rotation Sensor:
#     "Tekerlek ne kadar döndü?"
#
# Buradan:
#     "Robot ne kadar hareket etti?"
#
# hesaplanabilir.
#
# Daha sonra IMU ile:
#
# IMU:
#     "Robot hangi yönde?"
#
# Rotation Sensor:
#     "Robot ne kadar hareket etti?"
#
# bilgileri birleştirilerek robotun konumu tahmin edilebilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 14. ROTATION SENSOR vs IMU ROTATION
# ------------------------------------------------------------
#
# İsimler benzer olduğu için dikkat!
#
# IMU:
#
#     imu.rotation(DEGREES)
#
# Robotun / IMU'nun toplam açısal dönüşünü ölçer.
#
#
# Rotation Sensor:
#
#     rotation.position(DEGREES)
#
# Bağlı olduğu shaft'ın toplam dönüşünü ölçer.
#
# Bunlar AYNI ŞEY DEĞİLDİR.
# ------------------------------------------------------------


# ============================================================
# Ders 02 bitti, bir sonraki derse geçin.
# END OF 02 - ROTATION SENSOR
# ============================================================