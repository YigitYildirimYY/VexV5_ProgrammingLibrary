# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 04 - ROBOT COORDINATE SYSTEM
# ============================================================

from vex import *
from math import sin, cos, radians


brain = Brain()


# ------------------------------------------------------------
# KOORDİNAT SİSTEMİ
# ------------------------------------------------------------
#
# Robotun sahadaki konumunu X ve Y koordinatlarıyla
# ifade edebiliriz.
#
# Bu derste basit bir koordinat sistemi kullanıyoruz:
#
#              +Y
#               ↑
#               |
#               |
#               └────────→ +X
#
# Robot başlangıçta:
#
# X = 0
# Y = 0
#
# Heading = 0° kabul ediliyor ve bu modelde 0° yönü +X
# yönünü gösteriyor.
#
# Heading arttıkça robot saat yönünün tersine dönecek şekilde
# matematiksel koordinat sistemini kullanıyoruz.
# ------------------------------------------------------------

x = 0
y = 0
heading = 0


# ------------------------------------------------------------
# HAREKETİ X VE Y'YE AYIRMA
# ------------------------------------------------------------
#
# Robot bir mesafe ilerlediğinde bu hareketin tamamı her zaman
# sadece X veya sadece Y yönünde olmayabilir.
#
# Örneğin robot 45° yönünde 100 mm giderse hareketin bir
# kısmı X, bir kısmı Y yönündedir.
#
# Trigonometri ile:
#
#     x değişimi = distance × cos(heading)
#     y değişimi = distance × sin(heading)
#
# hesaplanabilir.
# ------------------------------------------------------------

def move_robot(distance):
    global x, y

    x += distance * cos(radians(heading))
    y += distance * sin(radians(heading))


# Robot 0° yönünde 500 mm ilerliyor.

move_robot(500)


# Şu anda:
#
# X = 500 mm
# Y = 0 mm


# Robotun yönünü 90° yapalım.

heading = 90


# 300 mm daha ilerliyor.

move_robot(300)


# Şimdi yaklaşık:
#
# X = 500 mm
# Y = 300 mm


# ------------------------------------------------------------
# SONUÇ
# ------------------------------------------------------------
#
# brain.screen.print() ile robotun tahmini konumunu
# görüntüleyebiliriz.
# ------------------------------------------------------------

brain.screen.print("X:", x)
brain.screen.next_row()
brain.screen.print("Y:", y)
brain.screen.next_row()
brain.screen.print("Heading:", heading)


# ------------------------------------------------------------
# GERÇEK ODOMETRY'DE
# ------------------------------------------------------------
#
# Burada distance ve heading değerlerini kendimiz verdik.
#
# Gerçek robotta:
#
# Rotation Sensor / Tracking Wheel
#     → Robot ne kadar hareket etti?
#
# IMU
#     → Robot hangi yöne bakıyor?
#
# Bu veriler kullanılarak x ve y sürekli güncellenir.
#
# Yani:
#
#     Ölçülen hareket
#            +
#        Heading
#            ↓
#       X ve Y hesabı
#
# şeklinde çalışır.
# ------------------------------------------------------------


# ============================================================
# Ders 04 bitti, bir sonraki derse geçin.
# END OF 04 - ROBOT COORDINATE SYSTEM
# ============================================================