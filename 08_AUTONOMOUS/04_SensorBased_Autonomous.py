# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 08 - AUTONOMOUS
# Yiğit YILDIRIM
# 04 - SENSOR BASED AUTONOMOUS
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

drivetrain = DriveTrain(left_drive, right_drive, 319.19, 320, 40, MM, 1.0)

distance = Distance(Ports.PORT6)

intake = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)


# ------------------------------------------------------------
# SENSOR BASED AUTONOMOUS NEDİR?
# ------------------------------------------------------------
#
# Normal autonomous'ta robot önceden belirlenmiş hareketleri
# sırayla yapar.
#
# Sensor-based autonomous'ta ise sensörlerden gelen bilgi
# programın kararlarını etkiler.
#
# Örneğin:
#
#     Nesne görünene kadar ilerle
#     Nesneye yaklaşınca dur
#     Intake'i çalıştır
#
# Burada robot yalnızca geçen süreye güvenmiyor; gerçekten
# sahada ne olduğunu kontrol ediyor.
# ------------------------------------------------------------


def autonomous():
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_stopping(BRAKE)

    drivetrain.drive(FORWARD)

    while True:
        if distance.is_object_detected():
            if distance.object_distance(MM) <= 150:
                break

        wait(20, MSEC)

    drivetrain.stop()

    intake.spin(FORWARD, 100, PERCENT)

    wait(500, MSEC)

    intake.stop(BRAKE)


# ------------------------------------------------------------
# DRIVER CONTROL
# ------------------------------------------------------------

def driver_control():
    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        left_drive.spin(FORWARD, left_speed, PERCENT)
        right_drive.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)


controller = Controller(PRIMARY)
competition = Competition(driver_control, autonomous)


# ============================================================
# Ders 04 bitti, bir sonraki derse geçin.
# END OF 04 - SENSOR BASED AUTONOMOUS
# ============================================================