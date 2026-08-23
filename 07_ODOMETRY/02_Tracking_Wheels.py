# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 02 - TRACKING WHEELS
# ============================================================

from vex import *


brain = Brain()


# ------------------------------------------------------------
# 1. TRACKING WHEEL NEDİR?
# ------------------------------------------------------------
#
# Tracking wheel, robotun hareketini ölçmek için kullanılan
# ve drivetrain'den bağımsız dönen bir tekerlektir.
#
# Bu tekerleğin amacı robotu hareket ettirmek değil,
# robotun ne kadar hareket ettiğini ölçmektir.
#
# Tracking wheel genellikle bir Rotation Sensor'a bağlanır.
# Böylece tekerleğin kaç tur veya kaç derece döndüğünü
# öğrenebiliriz.
#
# Örneğin robot ileri giderken tracking wheel de döner.
# Tekerleğin dönüşünden robotun aldığı mesafeyi hesaplayabiliriz.
# ------------------------------------------------------------


tracking = Rotation(Ports.PORT7)


# ------------------------------------------------------------
# 2. NEDEN DRIVETRAIN TEKERLEĞİNİ KULLANMIYORUZ?
# ------------------------------------------------------------
#
# Drivetrain tekerlekleri robotu hareket ettirirken aynı
# zamanda kayabilir.
#
# Örneğin robot 500 mm ilerlemek istediğinde tekerlekler
# zeminde biraz patinaj yaparsa encoder'ın gördüğü hareket
# gerçek hareketten farklı olabilir.
#
# Tracking wheel ise mümkün olduğunca bağımsız ve
# düşük kaymalı bir ölçüm tekerleği olarak tasarlanır.
#
# Böylece robotun gerçekten ne kadar hareket ettiğini
# daha güvenilir şekilde tahmin edebiliriz.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 3. TRACKING WHEEL'DEN MESAFE HESAPLAMA
# ------------------------------------------------------------
#
# Tracking wheel'in bir tam turda aldığı yol:
#
#     circumference = π × diameter
#
# Örneğin tekerlek çapı 50 mm ise:
#
#     circumference ≈ 157.1 mm
#
# Tekerlek 2 tur dönerse:
#
#     distance ≈ 314.2 mm
# ------------------------------------------------------------

wheel_diameter = 50
wheel_circumference = wheel_diameter * 3.14159


# ------------------------------------------------------------
# 4. ROTATION SENSOR'DAN VERİ OKUMA
# ------------------------------------------------------------
#
# position(TURNS), sensörün başlangıçtan beri toplam
# dönüşünü tur cinsinden verir.
# ------------------------------------------------------------

tracking.reset_position()

turns = tracking.position(TURNS)
distance = turns * wheel_circumference

brain.screen.print(distance)


# ------------------------------------------------------------
# 5. ODOMETRY'DE NEDEN ÖNEMLİ?
# ------------------------------------------------------------
#
# Tracking wheel bize "ne kadar hareket ettim?" bilgisini
# sağlar.
#
# Daha sonra IMU veya başka tracking wheel'lerden gelen
# bilgilerle bunu robotun yönü ve hareketiyle birleştiririz.
#
# Örneğin:
#
# Tracking wheel → Ne kadar ilerledim?
# IMU             → Hangi yöne bakıyorum?
#
# Bu bilgiler daha sonra X ve Y konumunu hesaplamak için
# kullanılabilir.
# ------------------------------------------------------------


# ============================================================
# Ders 02 bitti, bir sonraki derse geçin.
# END OF 02 - TRACKING WHEELS
# ============================================================