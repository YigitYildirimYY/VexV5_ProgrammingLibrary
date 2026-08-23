# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 06 - X_Y_POSITION
# ============================================================

from vex import *
from math import sin, cos, radians


brain = Brain()


# ------------------------------------------------------------
# X VE Y POSITION
# ------------------------------------------------------------
#
# Odometry'de robotun konumunu sürekli olarak:
#
#     X
#     Y
#     Heading
#
# şeklinde saklarız.
#
# Robot hareket ettiğinde alınan mesafeyi heading'e göre
# X ve Y yönlerine ayırıp mevcut konuma ekleriz.
# ------------------------------------------------------------

x = 0
y = 0
heading = 0


def update_position(distance):
    global x, y

    x += distance * cos(radians(heading))
    y += distance * sin(radians(heading))


# Robot başlangıçta (0, 0) noktasında.

update_position(500)

# Heading = 0° olduğu için 500 mm'nin tamamı X yönünde
# eklenir.


# Robot 90° döndü.

heading = 90

update_position(300)

# Bu kez hareket Y yönünde gerçekleşir.


# ------------------------------------------------------------
# KONUMU GÖRME
# ------------------------------------------------------------

brain.screen.clear_screen()
brain.screen.print(x)
brain.screen.next_row()
brain.screen.print(y)
brain.screen.next_row()
brain.screen.print(heading)


# ------------------------------------------------------------
# GERÇEK ODOMETRY'DE
# ------------------------------------------------------------
#
# Burada distance ve heading'i kendimiz verdik.
#
# Gerçek robotta:
#
# Rotation Sensor / tracking wheel → displacement
# IMU                           → heading
#
# verilerini sürekli okuyup update_position() gibi bir
# hesapla X ve Y'yi güncelleriz.
#
# Örneğin robot 45° yönünde hareket ediyorsa mesafenin bir
# kısmı X'e, bir kısmı Y'ye eklenir.
#
# Böylece robotun tahmini konumu zaman içinde takip edilir.
# ------------------------------------------------------------


# ============================================================
# Ders 06 bitti, bir sonraki derse geçin.
# END OF 06 - X Y POSITION
# ============================================================