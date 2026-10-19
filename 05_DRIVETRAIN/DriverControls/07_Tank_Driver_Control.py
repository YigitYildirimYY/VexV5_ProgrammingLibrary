# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 05 - DRIVETRAIN
# Yiğit YILDIRIM
# DriverControls
# 07 - TANK DRIVER CONTROL
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


# Tank Drive'da iki joystick doğrudan robotun iki tarafını
# kontrol eder. Bizim robotumuzdaki sürüş sistemi budur.
#
# axis3 → sol taraf
# axis2 → sağ taraf

while True:
    left_speed = controller.axis3.position()
    right_speed = controller.axis2.position()

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    wait(20, MSEC)

# Bu kod başlangıç seviyesi driver kontrolü kodudur. Çok bir şey beklemeyin :)
# ============================================================
# Ders 07 bitti, bir sonraki derse geçin.
# END OF 07 - TANK DRIVER CONTROL
# ============================================================
