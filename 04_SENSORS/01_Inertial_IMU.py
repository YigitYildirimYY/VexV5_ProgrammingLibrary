
# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 01 - INERTIAL IMU
# ============================================================




# VEX V5 Inertial Sensor:
# - Gyroscope (Jiroskop)
# - Accelerometer (İvmeölçer)
# - Heading
# - Rotation
#
# En temel kullanım amacı:
# Robotun yönünü ve dönüşünü algılamak.
#
# Özellikle:
# - Autonomous
# - Hassas dönüşler
# - Heading kontrolü
# - Odometry / localization
# için kullanılır.
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. SENSOR TANIMLAMA
# ------------------------------------------------------------

brain = Brain()

imu = Inertial(Ports.PORT6)


# ------------------------------------------------------------
# 2. CALIBRATION
# ------------------------------------------------------------
#
# Robot çalışırken IMU'nun kalibre edilmesi gerekir.
# Kalibrasyon sırasında robot HAREKETSİZ olmalıdır.
# ------------------------------------------------------------

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)


# ------------------------------------------------------------
# 3. HEADING
# ------------------------------------------------------------
#
# Heading, robotun hangi yöne baktığını derece cinsinden
# gösterir.
#
# Genellikle:
# 0°   → başlangıç yönü
# 90°  → 90 derece dönüş
# 180° → ters yön
# 270° → diğer yön
# ------------------------------------------------------------

heading = imu.heading(DEGREES)

brain.screen.print("Heading:", heading)


# ------------------------------------------------------------
# 4. ROTATION
# ------------------------------------------------------------
#
# Rotation, sensörün toplam ne kadar döndüğünü gösterir.
#
# Heading ile aynı şey değildir!
#
# Örneğin robot:
# 0° → 360° → 720°
#
# dönerse rotation değeri dönüşlerin toplamını takip edebilir.
# ------------------------------------------------------------

rotation = imu.rotation(DEGREES)

brain.screen.print("Rotation:", rotation)


# ------------------------------------------------------------
# 5. GYROSCOPE (JIROSKOP)
# ------------------------------------------------------------
#
# Jiroskop, sensörün açısal hareketini ölçer.
#
# VEX V5'te jiroskop, Inertial Sensor'ın içerisindedir.
# Ayrı bir fiziksel "gyro sensor" olarak düşünmemeliyiz.
#
# Gyroscope:
# "Robot ne kadar hızlı dönüyor?"
#
# Heading:
# "Robot şu anda hangi yöne bakıyor?"
#
# Bu ikisi aynı şey değildir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 6. ACCELEROMETER (İVMEÖLÇER)
# ------------------------------------------------------------
#
# Accelerometer, sensörün eksenlerindeki ivmeyi ölçer.
#
# Örneğin robot hızlanırken veya yavaşlarken değişimler
# meydana gelir.
#
# VEX'te bu da Inertial Sensor'ın içerisindedir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 7. PRACTICAL EXAMPLE
# ------------------------------------------------------------
#
# Robotun 90 derece dönmesini istiyoruz.
# ------------------------------------------------------------

imu.set_rotation(0, DEGREES)

# Burada robotun motorlarını çalıştırarak dönmesini sağlarız.
# Örnek:
#
# left_motor.spin(FORWARD)
# right_motor.spin(REVERSE)
#
# Sonrasında IMU ile dönüşü kontrol edebiliriz:

while imu.rotation(DEGREES) < 90:
    wait(10, MSEC)

# Dönüş tamamlandı.
#
# Gerçek robot kodunda motorları burada durdururuz.


# ------------------------------------------------------------
# 8. ÖNEMLİ KAVRAMLAR
# ------------------------------------------------------------
#
# Inertial Sensor:
#       
# 
#  Gyroscope       Açısal hareket
#  Accelerometer   İvme
#  Heading         Yön
#  Rotation        Toplam dönüş
#  
#
#
# IMU tek başına robotun sahadaki X/Y konumunu söylemez.
#
# Bunun için Rotation Sensor / encoder gibi başka
# sensörlerden gelen hareket bilgileriyle birlikte
# odometry / localization kullanılabilir.


# ============================================================
# Ders 01 bitti, bir sonraki derse geçin.
# END OF 01 - INERTIAL IMU
# ============================================================