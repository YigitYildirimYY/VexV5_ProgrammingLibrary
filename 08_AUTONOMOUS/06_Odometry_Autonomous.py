# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 06 - ODOMETRY AUTONOMOUS
# ============================================================

from vex import *


brain = Brain()

left_drive = MotorGroup(
    Motor(Ports.PORT1, GearSetting.RATIO_18_1, False),
    Motor(Ports.PORT2, GearSetting.RATIO_18_1, False),
    Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
)

right_drive = MotorGroup(
    Motor(Ports.PORT8, GearSetting.RATIO_18_1, True),
    Motor(Ports.PORT9, GearSetting.RATIO_18_1, True),
    Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
)

left_tracking = Rotation(Ports.PORT6)
right_tracking = Rotation(Ports.PORT7)
imu = Inertial(Ports.PORT9)


# ------------------------------------------------------------
# ODOMETRY + AUTONOMOUS
# ------------------------------------------------------------
#
# Burada odometry'nin autonomous içinde nasıl kullanıldığını
# gösteriyoruz.
#
# Tracking wheel'ler robotun ne kadar ilerlediğini ölçüyor.
# IMU robotun heading'ini takip ediyor.
#
# Bu örnekte robot sadece başlangıç yönünde ilerliyor.
# Yani henüz X-Y arasında hedef seçip oraya yönelmiyoruz.
#
# Amaç:
#
# "Robot gerçekten 1000 mm'ye ulaştı mı?"
#
# sorusunu sensörlerden cevaplamak.
# ------------------------------------------------------------

WHEEL_DIAMETER = 50
WHEEL_CIRCUMFERENCE = 3.14159 * WHEEL_DIAMETER

TARGET_DISTANCE = 1000

x = 0
y = 0

last_left = 0
last_right = 0


def reset_odometry():
    global x, y, last_left, last_right

    x = 0
    y = 0

    left_tracking.reset_position()
    right_tracking.reset_position()

    last_left = left_tracking.position(DEGREES)
    last_right = right_tracking.position(DEGREES)


def update_odometry():
    global x, y, last_left, last_right

    current_left = left_tracking.position(DEGREES)
    current_right = right_tracking.position(DEGREES)

    left_delta = current_left - last_left
    right_delta = current_right - last_right

    left_distance = left_delta / 360 * WHEEL_CIRCUMFERENCE
    right_distance = right_delta / 360 * WHEEL_CIRCUMFERENCE

    forward_distance = (left_distance + right_distance) / 2

    x += forward_distance

    last_left = current_left
    last_right = current_right


# ------------------------------------------------------------
# AUTONOMOUS
# ------------------------------------------------------------
#
# Robot ileri giderken odometry sürekli güncelleniyor.
#
# Robot 1000 mm'ye ulaştığında duruyor.
#
# Burada önemli olan, "1 saniye sür" veya "motoru şu kadar
# çalıştır" demememiz.
#
# Robotun gerçekten ne kadar ilerlediğini ölçüyoruz.
# ------------------------------------------------------------

def autonomous():
    reset_odometry()

    left_drive.spin(FORWARD, 40, PERCENT)
    right_drive.spin(FORWARD, 40, PERCENT)

    while True:
        update_odometry()

        if x >= TARGET_DISTANCE:
            break

        wait(20, MSEC)

    left_drive.stop(BRAKE)
    right_drive.stop(BRAKE)


# ------------------------------------------------------------
# SONUÇ
# ------------------------------------------------------------
#
# Bu örnekte odometry robotu hedefe yönlendirmiyor.
#
# Sadece autonomous'a:
#
#     "Şu anda yaklaşık X = ... mm konumundasın."
#
# bilgisini sağlıyor.
#
# Daha gelişmiş bir sistemde bu bilgiye hedef konum, heading
# kontrolü ve PID eklenerek gerçek point-to-point navigation
# yapılabilir.
# ------------------------------------------------------------


autonomous()


# ============================================================
# Ders 06 bitti, bir sonraki derse geçin.
# END OF 06 - ODOMETRY AUTONOMOUS
# ============================================================