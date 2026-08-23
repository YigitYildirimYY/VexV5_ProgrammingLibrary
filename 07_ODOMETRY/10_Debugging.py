# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 10 - ODOMETRY DEBUGGING
# ============================================================

from vex import *


brain = Brain()

left_tracking = Rotation(Ports.PORT7)
right_tracking = Rotation(Ports.PORT8)
imu = Inertial(Ports.PORT9)


# ------------------------------------------------------------
# ODOMETRY DEBUGGING NEDİR?
# ------------------------------------------------------------
#
# Odometry'de robotun gerçek konumu ile hesaplanan konumu
# birbirinden farklı olabilir.
#
# Bu yüzden önce sensörlerin gerçekten doğru veri verip
# vermediğine bakmalıyız.
#
# En önemli değerler:
#
# left_tracking  → sol tracking wheel
# right_tracking → sağ tracking wheel
# heading        → IMU yönü
#
# Sorunun sensörde mi, ölçülerde mi yoksa hesaplamada mı
# olduğunu bu değerleri izleyerek bulabiliriz.
# ------------------------------------------------------------


left_tracking.reset_position()
right_tracking.reset_position()

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)


# ------------------------------------------------------------
# SENSORLARI TEST ETME
# ------------------------------------------------------------
#
# Robot hareketsizken tracking wheel'lerin position değerleri
# değişmemelidir.
#
# Robotu elle ileri götürdüğümüzde iki tracking wheel'in
# değerleri hareket yönüne uygun şekilde değişmelidir.
#
# Robotu döndürdüğümüzde ise sol ve sağ tracking wheel
# değerlerinin birbirinden farklı değişmesi normaldir.
#
# IMU heading'i de robot döndükçe değişmelidir.
# ------------------------------------------------------------

while True:
    left_position = left_tracking.position(DEGREES)
    right_position = right_tracking.position(DEGREES)
    heading = imu.heading(DEGREES)

    brain.screen.clear_screen()

    brain.screen.print("Left: ", left_position)
    brain.screen.next_row()

    brain.screen.print("Right: ", right_position)
    brain.screen.next_row()

    brain.screen.print("Heading: ", heading)

    wait(100, MSEC)


# ------------------------------------------------------------
# SORUNU NASIL BULURUZ?
# ------------------------------------------------------------
#
# Robot hareket etmiyor ama encoder değeri değişiyorsa:
# Tracking wheel veya montajı kontrol edilmelidir.
#
# Robot ileri giderken bir tracking wheel negatif değer
# veriyorsa:
# Sensörün yönü ters olabilir.
#
# Robot sabitken heading sürekli değişiyorsa:
# IMU kalibrasyonu ve sensör montajı kontrol edilmelidir.
#
# Robot doğru hareket ettiği halde X/Y yanlış hesaplanıyorsa:
# Tekerlek çapı, ölçüm mesafeleri, yön işaretleri veya
# koordinat hesabı kontrol edilmelidir.
#
# Robot döndükten sonra konumu belirgin şekilde kayıyorsa:
# Tracking wheel'lerin yerleşimi ve dönüşten kaynaklanan
# geometrik etkiler hesaba katılmalıdır.
# ------------------------------------------------------------


# ------------------------------------------------------------
# ODOMETRY DEBUGGING'İN TEMEL KURALI
# ------------------------------------------------------------
#
# Önce sensörleri test et.
# Sonra ölçüleri kontrol et.
# Sonra matematiği kontrol et.
#
# Her şey doğruysa ancak o zaman odometry kodunu değiştirmek
# gerekir.
#
# Böylece "X yanlış çıkıyor" gibi bir problemi doğrudan
# formülleri değiştirerek çözmeye çalışmayız.
# ------------------------------------------------------------


# ============================================================
# Ders 10 bitti, bir sonraki derse geçin.
# END OF 10 - ODOMETRY DEBUGGING
# ============================================================