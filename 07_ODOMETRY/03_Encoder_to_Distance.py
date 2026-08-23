# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 03 - ENCODER TO DISTANCE
# ============================================================

from vex import *


brain = Brain()

tracking = Rotation(Ports.PORT7)


# ------------------------------------------------------------
# 1. ENCODER'DAN MESAFEYE
# ------------------------------------------------------------
#
# Rotation Sensor bize tracking wheel'in kaç tur döndüğünü
# söyleyebilir.
#
# Bir tam turda tekerleğin aldığı yol, tekerleğin çevresidir:
#
#     circumference = π × diameter
#
# Örneğin çapı 50 mm olan bir tekerlek:
#
#     circumference ≈ 157.1 mm
#
# 2 tur dönerse:
#
#     distance ≈ 314.2 mm
# ------------------------------------------------------------

wheel_diameter = 50
wheel_circumference = 3.14159 * wheel_diameter


# ------------------------------------------------------------
# 2. POSITION'I SIFIRLAMA
# ------------------------------------------------------------
#
# Odometry'ye başlarken tracking wheel'in mevcut konumunu
# 0 kabul etmek istiyoruz.
# ------------------------------------------------------------

tracking.reset_position()


# ------------------------------------------------------------
# 3. DÖNÜŞÜ MESAFEYE ÇEVİRME
# ------------------------------------------------------------

turns = tracking.position(TURNS)
distance = turns * wheel_circumference

brain.screen.print(distance)


# ------------------------------------------------------------
# 4. NE ANLAMA GELİYOR?
# ------------------------------------------------------------
#
# Örneğin:
#
#     turns = 1
#
# ise tracking wheel bir tam tur dönmüştür.
#
# 50 mm çapındaki tekerlek için:
#
#     distance = 1 × 157.1
#              ≈ 157.1 mm
#
# 3 tur için:
#
#     distance ≈ 471.2 mm
#
# Böylece sensörün ölçtüğü dönüşü robotun aldığı mesafeye
# çevirmiş oluyoruz.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 5. ODOMETRY'DEKİ YERİ
# ------------------------------------------------------------
#
# Şu anda sadece "ne kadar hareket ettik?" sorusunu
# cevaplayabiliyoruz.
#
# Örneğin:
#
#     Rotation Sensor
#            ↓
#       tur sayısı
#            ↓
#       mesafe (mm)
#
# Bir sonraki aşamada bu mesafeyi robotun heading'i ile
# birleştirerek X ve Y konumunu hesaplayacağız.
# ------------------------------------------------------------


# ============================================================
# Ders 03 bitti, bir sonraki derse geçin.
# END OF 03 - ENCODER TO DISTANCE
# ============================================================