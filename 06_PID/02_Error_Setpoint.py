# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 06 - PID CONTROL
# Yiğit YILDIRIM
# 02 - ERROR AND SETPOINT
# ============================================================

from vex import *


brain = Brain()

imu = Inertial(Ports.PORT7)


# ------------------------------------------------------------
# SETPOINT, CURRENT VE ERROR NEDİR?
# ------------------------------------------------------------
#
# Setpoint (target), ulaşmak istediğimiz değerdir.
#
# Current, sensörden o anda okuduğumuz gerçek değerdir.
#
# Error ise hedef ile mevcut değer arasındaki farktır.
#
# Formül:
#
#     error = target - current
#
# Örneğin:
#
#     target = 90°
#     current = 70°
#
#     error = 90 - 70
#           = 20°
#
# Robot hedefin 20° gerisindedir.
# ------------------------------------------------------------

target = 90


imu.calibrate()

while imu.is_calibrating():
    wait(20, MSEC)

imu.reset_rotation()


# Robotu döndürmeye başlıyoruz. Burada amaç sadece
# sensörden current ve error değerlerini görmektir.

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

left_drive.spin(FORWARD, 20, PERCENT)
right_drive.spin(REVERSE, 20, PERCENT)


# ------------------------------------------------------------
# ERROR'U SÜREKLİ HESAPLAMA
# ------------------------------------------------------------
#
# Robot döndükçe current değişir.
# Current değiştikçe error da değişir.
#
# Örneğin:
#
# current = 30°  → error = 60°
# current = 60°  → error = 30°
# current = 80°  → error = 10°
# current = 89°  → error = 1°
#
# Yani robot hedefe yaklaştıkça error küçülür.
# ------------------------------------------------------------

while True:
    current = imu.rotation(DEGREES)
    error = target - current

    brain.screen.clear_screen()
    brain.screen.print("Target:", target)
    brain.screen.next_row()
    brain.screen.print("Current:", current)
    brain.screen.next_row()
    brain.screen.print("Error:", error)

    if abs(error) <= 1:
        break

    wait(20, MSEC)


left_drive.stop(BRAKE)
right_drive.stop(BRAKE)


# ------------------------------------------------------------
# NEDEN ERROR ÖNEMLİ?
# ------------------------------------------------------------
#
# PID'nin daha sonra vereceği motor çıktısının temelini
# error oluşturur.
#
# Büyük error:
#     Hedeften çok uzaktayız.
#
# Küçük error:
#     Hedefe yakınız.
#
# error = 0:
#     Hedefe ulaştık.
#
# Bir sonraki derste P kontrolünde bunu kullanacağız:
#
#     output = Kp × error
#
# Böylece motor gücü doğrudan hatanın büyüklüğüne
# bağlanmış olacak.
# ------------------------------------------------------------


# ============================================================
# Ders 02 bitti, bir sonraki derse geçin.
# END OF 02 - ERROR AND SETPOINT
# ============================================================