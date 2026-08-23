# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 07 - GPS SENSOR
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. GPS SENSOR NEDİR?
# ------------------------------------------------------------
#
# VEX V5 GPS Sensor, robotun VEX sahasındaki konumunu ve
# yönünü gerçek zamanlı olarak belirlemek için kullanılır.
#
# Sensör, sahanın kenarlarında bulunan GPS Field Code'u
# kullanarak robotun X ve Y koordinatlarını ve heading'ini
# hesaplar.
#
# Bu yüzden GPS Sensor:
#
# - Robotun X konumunu
# - Robotun Y konumunu
# - Robotun saha üzerindeki heading'ini
# öğrenmemizi sağlar.
#
# GPS Sensor özellikle autonomous ve localization
# sistemlerinde çok kullanışlıdır.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. SENSOR TANIMLAMA
# ------------------------------------------------------------

brain = Brain()

gps = Gps(Ports.PORT7)


# ------------------------------------------------------------
# 3. CALIBRATION
# ------------------------------------------------------------
#
# calibrate(), GPS Sensor'ın referans heading'ini robotun
# mevcut drivetrain heading'ine göre ayarlar.
#
# Kalibrasyon sırasında robot tamamen hareketsiz olmalıdır.
# ------------------------------------------------------------

gps.calibrate()


# ------------------------------------------------------------
# 4. X VE Y POSITION
# ------------------------------------------------------------
#
# x_position() ve y_position(), GPS Sensor'ın reference
# point'inin sahadaki koordinatlarını verir.
#
# MM veya INCHES kullanabiliriz.
# ------------------------------------------------------------

x = gps.x_position(MM)
y = gps.y_position(MM)

brain.screen.print(x)
brain.screen.print(y)


# ------------------------------------------------------------
# 5. HEADING
# ------------------------------------------------------------
#
# heading(), robotun saha koordinat sistemine göre yönünü
# 0 ile 359.9 derece arasında verir.
#
# Buradaki heading, IMU'daki gibi yalnızca sensörün kendi
# dönüş referansına göre değil, GPS Field'in yönüne göre
# belirlenen absolute field heading'dir.
#
# 0° saha üzerindeki 12 yönünü temsil eder ve değerler
# saat yönünde artar.
# ------------------------------------------------------------

heading = gps.heading()

brain.screen.print(heading)


# ------------------------------------------------------------
# 6. X, Y VE HEADING BİRLİKTE
# ------------------------------------------------------------
#
# Robotun konumunu ve yönünü birlikte okuyabiliriz.
# ------------------------------------------------------------

x = gps.x_position(MM)
y = gps.y_position(MM)
heading = gps.heading()

brain.screen.print(x)
brain.screen.print(y)
brain.screen.print(heading)


# ------------------------------------------------------------
# 7. SET_ORIGIN
# ------------------------------------------------------------
#
# set_origin(), GPS Sensor'ın robot üzerindeki reference
# point'inin konumunu tanımlar.
#
# Örneğin GPS Sensor'ın fiziksel konumunun reference
# point'ten 25 mm ileride olduğunu söyleyebiliriz.
# ------------------------------------------------------------

gps.set_origin(0, 25, MM)


# ------------------------------------------------------------
# 8. SET_LOCATION
# ------------------------------------------------------------
#
# set_location(), reference point'in sahadaki X ve Y
# konumunu ve heading'ini manuel olarak ayarlar.
#
# Bu özellikle robotun başlangıçta Field Code'u yeterince
# iyi göremediği durumlarda konumu manuel olarak belirlemek
# için kullanılabilir.
# ------------------------------------------------------------

gps.set_location(0, 0, MM, 0, DEGREES)


# ------------------------------------------------------------
# 9. GPS QUALITY
# ------------------------------------------------------------
#
# quality(), GPS Sensor'ın sinyal kalitesini yüzde olarak
# verir.
#
# Yüksek değerler daha güvenilir GPS verisi anlamına gelir.
#
# Değer 0'a yaklaştıkça sensörün konum verisine olan
# güven azalır.
# ------------------------------------------------------------

quality = gps.quality()

brain.screen.print(quality)


# ------------------------------------------------------------
# 10. ACCELERATION
# ------------------------------------------------------------
#
# GPS Sensor'ın acceleration() methodu, seçilen eksendeki
# ivmeyi G cinsinden verir.
#
# X, Y veya Z ekseni seçilebilir.
# ------------------------------------------------------------

acceleration = gps.acceleration(AxisType.XAXIS)

brain.screen.print(acceleration)


# ------------------------------------------------------------
# 11. GYRO RATE
# ------------------------------------------------------------
#
# gyro_rate(), seçilen eksendeki açısal dönüş hızını verir.
#
# Birim olarak:
#
# VelocityUnits.DPS
# VelocityUnits.RPM
#
# kullanılabilir.
# ------------------------------------------------------------

gyro_rate = gps.gyro_rate(
    AxisType.ZAXIS,
    VelocityUnits.DPS
)

brain.screen.print(gyro_rate)


# ------------------------------------------------------------
# 12. ORIENTATION
# ------------------------------------------------------------
#
# orientation(), robotun roll, pitch veya yaw değerini
# derece cinsinden verir.
#
# Roll:
# Robotun yanlara doğru eğimi
#
# Pitch:
# Robotun öne veya arkaya doğru eğimi
#
# Yaw:
# Robotun dikey ekseni etrafındaki yönelimi
# ------------------------------------------------------------

yaw = gps.orientation(
    OrientationType.YAW,
    DEGREES
)

brain.screen.print(yaw)


# ------------------------------------------------------------
# 13. GPS İLE ROBOTUN KONUMUNU ÖĞRENME
# ------------------------------------------------------------
#
# Örneğin robotun sahadaki mevcut konumunu okuyabiliriz.
# ------------------------------------------------------------

x = gps.x_position(MM)
y = gps.y_position(MM)

if gps.quality() > 90:
    brain.screen.print(x)
    brain.screen.print(y)


# ------------------------------------------------------------
# 14. GPS VE IMU FARKI
# ------------------------------------------------------------
#
# IMU temel olarak robotun kendi hareketini ve yönelimini
# ölçer.
#
# GPS Sensor ise robotun sahadaki konumunu, yani X ve Y
# koordinatlarını da belirleyebilir.
#
# Örneğin:
#
# IMU:
# Robot hangi yönde?
#
# GPS:
# Robot sahada nerede ve hangi yönde?
#
# Bu nedenle GPS, localization konusunda çok güçlü bir
# sensördür.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 15. ODOMETRY İLE İLİŞKİSİ
# ------------------------------------------------------------
#
# Rotation Sensor ve IMU kullanılarak oluşturulan odometry,
# robotun hareketinden konum tahmini yapar.
#
# GPS Sensor ise sahadaki gerçek konumu doğrudan ölçmeye
# yardımcı olur.
#
# Bu nedenle gelişmiş sistemlerde GPS ve odometry birlikte
# kullanılabilir.
# ------------------------------------------------------------


# ============================================================
# Ders 07 bitti, bir sonraki derse geçin.
# END OF 07 - GPS SENSOR
# ============================================================