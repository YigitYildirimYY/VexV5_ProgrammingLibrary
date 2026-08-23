# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 07 - ODOMETRY
# Yiğit YILDIRIM
# 08 - 3-WHEEL ODOMETRY
# ============================================================

from vex import *
from math import sin, cos, radians


brain = Brain()

left_tracking = Rotation(Ports.PORT7)
right_tracking = Rotation(Ports.PORT8)
horizontal_tracking = Rotation(Ports.PORT9)

imu = Inertial(Ports.PORT10)


# ------------------------------------------------------------
# 3-WHEEL ODOMETRY NEDİR?
# ------------------------------------------------------------
#
# 3-wheel odometry'de robotun hareketini ölçmek için
# drivetrain'den bağımsız üç tracking wheel kullanılır.
#
# Sol ve sağ tracking wheel:
#     Robotun ileri / geri hareketini ölçer.
#
# Horizontal tracking wheel:
#     Robotun sağa / sola hareketini ölçer.
#
# IMU:
#     Robotun heading bilgisini verir.
#
# Bu bilgileri birleştirerek robotun:
#
#     X
#     Y
#     Heading
#
# konumunu sürekli olarak takip edebiliriz.
# ------------------------------------------------------------


wheel_diameter = 50
wheel_circumference = 3.14159 * wheel_diameter

horizontal_offset = 100


x = 0
y = 0


# ------------------------------------------------------------
# SENSORLARI SIFIRLAMA
# ------------------------------------------------------------
#
# Odometry başlarken bütün tracking wheel'leri sıfırdan
# başlatmak işimizi kolaylaştırır.
# ------------------------------------------------------------

left_tracking.reset_position()
right_tracking.reset_position()
horizontal_tracking.reset_position()

imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)


last_left = left_tracking.position(DEGREES)
last_right = right_tracking.position(DEGREES)
last_horizontal = horizontal_tracking.position(DEGREES)


# ------------------------------------------------------------
# ODOMETRY DÖNGÜSÜ
# ------------------------------------------------------------

while True:
    current_left = left_tracking.position(DEGREES)
    current_right = right_tracking.position(DEGREES)
    current_horizontal = horizontal_tracking.position(DEGREES)

    left_delta = current_left - last_left
    right_delta = current_right - last_right
    horizontal_delta = current_horizontal - last_horizontal


    # Her tracking wheel'in dönüşünü mesafeye çeviriyoruz.

    left_distance = left_delta / 360 * wheel_circumference
    right_distance = right_delta / 360 * wheel_circumference
    horizontal_distance = horizontal_delta / 360 * wheel_circumference


    # Sol ve sağ wheel'lerin ortalaması robotun ileri-geri
    # hareketini verir.

    forward_distance = (left_distance + right_distance) / 2


    # IMU'dan robotun mevcut heading'ini alıyoruz.

    heading = imu.heading(DEGREES)
    angle = radians(heading)


    # Robotun dönüşünden dolayı horizontal tracking wheel'de
    # de hareket görülür. Offset kullanarak bu kısmı düzeltiriz.

    rotation = radians(heading)

    strafe_distance = horizontal_distance - (
        horizontal_offset * rotation
    )


    # Robotun kendi koordinat sistemindeki hareketini
    # saha koordinat sistemine çeviriyoruz.

    delta_x = (
        forward_distance * cos(angle)
        - strafe_distance * sin(angle)
    )

    delta_y = (
        forward_distance * sin(angle)
        + strafe_distance * cos(angle)
    )


    x += delta_x
    y += delta_y


    last_left = current_left
    last_right = current_right
    last_horizontal = current_horizontal


    # --------------------------------------------------------
    # DEBUG
    # --------------------------------------------------------

    brain.screen.clear_screen()
    brain.screen.print("X: ", x)
    brain.screen.next_row()
    brain.screen.print("Y: ", y)
    brain.screen.next_row()
    brain.screen.print("Heading: ", heading)

    wait(20, MSEC)


# ============================================================
# Ders 08 bitti, bir sonraki derse geçin.
# END OF 08 - 3-WHEEL ODOMETRY
# ============================================================