# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 01 - WHAT IS ODOMETRY
# ============================================================

from vex import *
from math import sin, cos, radians


brain = Brain()


# ------------------------------------------------------------
# ODOMETRY NEDİR?
# ------------------------------------------------------------
#
# Odometry, robotun hareketini takip ederek robotun sahada
# nerede olduğunu tahmin etme yöntemidir.
#
# Robotun konumunu üç temel değerle ifade edebiliriz:
#
# X       → robotun yatay konumu
# Y       → robotun dikey konumu
# Heading → robotun baktığı yön
#
# Örneğin:
#
# X = 500 mm
# Y = 300 mm
# Heading = 90°
#
# robotun sahada nerede olduğunu ve hangi yöne baktığını
# ifade eder.
# ------------------------------------------------------------


x = 0
y = 0
heading = 0


# ------------------------------------------------------------
# ROBOT HAREKET ETTİĞİNDE NE OLUR?
# ------------------------------------------------------------
#
# Robot bir mesafe kat ettiğinde, bu hareket robotun
# heading'ine göre X ve Y bileşenlerine ayrılır.
#
# Örneğin robot 100 mm ileri gidiyorsa:
#
# Heading = 0°
# X yönünde hareket eder.
#
# Heading = 90°
# Y yönünde hareket eder.
#
# Dolayısıyla robotun aldığı yolu ve yönünü bilirsek
# yeni X ve Y konumunu hesaplayabiliriz.
# ------------------------------------------------------------


def move_robot(distance, heading):
    global x, y

    x += distance * cos(radians(heading))
    y += distance * sin(radians(heading))


# Robot başlangıçta (0, 0) noktasında.

move_robot(500, 0)

brain.screen.print(x)
brain.screen.next_row()
brain.screen.print(y)


# Robot daha sonra 90° dönüp 300 mm ilerlesin.

move_robot(300, 90)


brain.screen.clear_screen()
brain.screen.print(x)
brain.screen.next_row()
brain.screen.print(y)


# ------------------------------------------------------------
# GERÇEK ODOMETRY'DE NE DEĞİŞİYOR?
# ------------------------------------------------------------
#
# Yukarıdaki örnekte distance ve heading değerlerini
# kendimiz verdik.
#
# Gerçek robotta bunları sensörlerden elde ederiz.
#
# Rotation Sensor / Encoder:
# Robot veya tracking wheel ne kadar hareket etti?
#
# IMU:
# Robot hangi yönde?
#
# Bu bilgileri sürekli birleştirerek X, Y ve heading
# değerlerini güncelleriz.
#
# Yani gerçek sistem kabaca:
#
# Sensörler
#     ↓
# Hareket miktarı + Heading
#     ↓
# Odometry hesabı
#     ↓
# X, Y, Heading
#
# şeklinde çalışır.
# ------------------------------------------------------------


# ============================================================
# Ders 01 bitti, bir sonraki derse geçin.
# END OF 01 - WHAT IS ODOMETRY
# ============================================================