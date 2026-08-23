# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 07 - IMU AND ODOMETRY
# ============================================================

from vex import *
from math import sin, cos, radians


brain = Brain()

tracking = Rotation(Ports.PORT7)
imu = Inertial(Ports.PORT8)


# ------------------------------------------------------------
# IMU + ODOMETRY
# ------------------------------------------------------------
#
# Rotation Sensor bize tracking wheel'in ne kadar döndüğünü,
# yani robotun ne kadar hareket ettiğini söyler.
#
# IMU ise robotun heading'ini verir.
#
# Bu iki bilgiyi birleştirerek hareketi X ve Y eksenlerine
# ayırabilir ve robotun konumunu takip edebiliriz.
#
# Bu örnekte 0° yönünü +X kabul ediyoruz.
# ------------------------------------------------------------

wheel_diameter = 50
wheel_circumference = 3.14159 * wheel_diameter

x = 0
y = 0

tracking.reset_position()

imu.calibrate()


# Kalibrasyon sırasında robot hareketsiz kalmalıdır.

while imu.is_calibrating():
    wait(20, MSEC)


last_position = tracking.position(DEGREES)


# ------------------------------------------------------------
# ODOMETRY LOOP
# ------------------------------------------------------------
#
# Her döngüde tracking wheel'in yeni konumunu okuyoruz.
# İki okuma arasındaki fark bize ne kadar hareket ettiğimizi
# gösteriyor.
#
# Sonra IMU heading'ini kullanarak bu hareketi X ve Y'ye
# dağıtıyoruz.
# ------------------------------------------------------------

while True:
    current_position = tracking.position(DEGREES)
    delta_degrees = current_position - last_position

    distance = (delta_degrees / 360) * wheel_circumference

    heading = imu.heading(DEGREES)
    angle = radians(heading)

    x += distance * cos(angle)
    y += distance * sin(angle)

    last_position = current_position

    brain.screen.clear_screen()
    brain.screen.print("X: ", x)
    brain.screen.next_row()
    brain.screen.print("Y: ", y)
    brain.screen.next_row()
    brain.screen.print("Heading: ", heading)

    wait(20, MSEC)


# ============================================================
# Ders 07 bitti, bir sonraki derse geçin.
# END OF 07 - IMU AND ODOMETRY
# ============================================================