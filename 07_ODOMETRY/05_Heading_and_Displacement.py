# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 05 - HEADING AND DISPLACEMENT
# ============================================================

from vex import *
from math import sin, cos, radians


brain = Brain()


# ------------------------------------------------------------
# HEADING VE DISPLACEMENT NEDİR?
# ------------------------------------------------------------
#
# Heading, robotun hangi yöne baktığını gösterir.
#
# Displacement ise robotun ne kadar yer değiştirdiğidir.
#
# Odometry'de bu ikisini birlikte kullanırız:
#
#     Heading     → Hangi yönde?
#     Displacement → Ne kadar?
#
# Örneğin robot 500 mm ilerlediyse bu hareketin X ve Y
# bileşenlerini heading'e göre hesaplayabiliriz.
# ------------------------------------------------------------


x = 0
y = 0
heading = 45
distance = 500


# ------------------------------------------------------------
# HAREKETİ X VE Y'YE AYIRMA
# ------------------------------------------------------------
#
# Robot 45° yönünde 500 mm hareket ediyor.
#
# Hareketin tamamı yalnızca X veya Y yönünde değildir.
# İki eksende de ilerleme vardır.
#
#     delta_x = distance × cos(heading)
#     delta_y = distance × sin(heading)
# ------------------------------------------------------------

delta_x = distance * cos(radians(heading))
delta_y = distance * sin(radians(heading))

x += delta_x
y += delta_y


brain.screen.print("Delta X:", delta_x)
brain.screen.next_row()
brain.screen.print("Delta Y:", delta_y)
brain.screen.next_row()
brain.screen.print("X:", x)
brain.screen.next_row()
brain.screen.print("Y:", y)


# ------------------------------------------------------------
# GERÇEK ROBOTTA
# ------------------------------------------------------------
#
# Buradaki distance değerini kendimiz verdik.
#
# Gerçek odometry'de bu değer tracking wheel veya encoder
# verilerinden gelir.
#
# Heading ise IMU gibi bir sensörden alınabilir.
#
# Örneğin:
#
#     Tracking Wheel → displacement
#     IMU            → heading
#
# Bu iki bilgi birleştirilerek robotun yeni X ve Y
# konumu hesaplanabilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# NEDEN SADECE MESAFE YETMEZ?
# ------------------------------------------------------------
#
# Robot 500 mm hareket ettiğini bilirse ne kadar gittiğini
# bilir, fakat nereye gittiğini bilmez.
#
# 500 mm kuzeye gitmek ile 500 mm doğuya gitmek aynı
# displacement değerine sahiptir fakat X ve Y konumları
# farklıdır.
#
# Bu yüzden displacement tek başına yeterli değildir.
# Heading ile birlikte kullanılması gerekir.
# ------------------------------------------------------------


# ============================================================
# Ders 05 bitti, bir sonraki derse geçin.
# END OF 05 - HEADING AND DISPLACEMENT
# ============================================================