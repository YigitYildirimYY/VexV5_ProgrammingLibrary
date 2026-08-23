# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 02 - COMPETITION TEMPLATE
# ============================================================

from vex import *


brain = Brain()
controller = Controller(PRIMARY)

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

drivetrain = DriveTrain(left_drive, right_drive, 319.19, 320, 40, MM, 1.0)


# ------------------------------------------------------------
# AUTONOMOUS
# ------------------------------------------------------------
#
# Yarışmanın autonomous kısmında sürücü Controller'ı
# kullanmaz. Robot burada önceden yazılmış komutları uygular.
# ------------------------------------------------------------

def autonomous():
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_turn_velocity(40, PERCENT)
    drivetrain.set_stopping(BRAKE)

    drivetrain.drive_for(FORWARD, 500, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)

    drivetrain.stop()


# ------------------------------------------------------------
# DRIVER CONTROL
# ------------------------------------------------------------
#
# Driver Control başladığında robotu sürücü kontrol eder.
#
# Bizim robotumuz Tank Drive kullandığı için iki joysticki
# drivetrain'in iki tarafına bağlıyoruz.
# ------------------------------------------------------------

def driver_control():
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        left_drive.spin(FORWARD, left_speed, PERCENT)
        right_drive.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)


# ------------------------------------------------------------
# COMPETITION CONTROL
# ------------------------------------------------------------
#
# Competition nesnesi autonomous() ve driver_control()
# fonksiyonlarını yarışma sistemine bağlar.
#
# Yarışma autonomous moduna geçtiğinde autonomous(),
# Driver Control moduna geçtiğinde driver_control()
# çalıştırılır.
# ------------------------------------------------------------

competition = Competition(driver_control, autonomous)


# ============================================================
# Ders 02 bitti, bir sonraki derse geçin.
# END OF 02 - COMPETITION TEMPLATE
# ============================================================