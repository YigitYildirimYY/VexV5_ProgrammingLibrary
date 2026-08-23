# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 07 - MOTOR POWER
# ============================================================

from vex import *


brain = Brain()

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)


# ============================================================
# 01 - POWER NEDİR?
# ============================================================

# Power (güç), motorun elektrik enerjisini ne kadar hızlı
# kullandığını ifade eder.
#
# VEX Motor'da power Watt (W) cinsinden okunabilir.
#
# Genel olarak:
#
#     Daha fazla yük
#          ↓
#     Daha fazla güç tüketimi
#
# Power ile torque aynı şey değildir.
#
# Torque:
#     Döndürme kuvveti
#
# Power:
#     Enerji kullanım hızı


# ============================================================
# 02 - POWER OKUMA
# ============================================================

power = motor.power()

print(power)

# power() motorun kullandığı gücü Watt cinsinden döndürür.
#
# Açık şekilde birim vermek istersek:
#
#     motor.power(PowerUnits.WATT)
#
# kullanabiliriz.


# ============================================================
# 03 - MOTOR ÇALIŞIRKEN POWER OKUMA
# ============================================================

motor.spin(FORWARD, 50, PERCENT)

wait(500, MSEC)

power = motor.power(PowerUnits.WATT)

print(power)

motor.stop()


# ============================================================
# 04 - POWER'I EKRANDA GÖRME
# ============================================================

motor.spin(FORWARD, 50, PERCENT)

while True:

    power = motor.power(PowerUnits.WATT)

    brain.screen.clear_screen()
    brain.screen.print(f"Power: {power} W")

    wait(100, MSEC)


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Gücü oku:
#
#     motor.power()
#
# veya:
#
#     motor.power(PowerUnits.WATT)
#
#
# Birim:
#
#     Watt (W)
#
#
# Power:
#     Motorun elektrik enerjisini ne kadar hızlı
#     kullandığını gösterir.
#
#
# Torque:
#     Motorun döndürme kuvveti.
#
#
# Current:
#     Motorun çektiği elektrik akımı.
#
#
# Bu üç değer birbirinden farklıdır:
#
#     Current → Akım
#     Power   → Güç
#     Torque  → Tork
#
#
# Power özellikle:
#
#     Motor yükünü gözlemleme
#     Debugging
#     Mekanizma performansını inceleme
#
# gibi durumlarda kullanılabilir.


# ============================================================
# Ders 07 bitti, bir sonraki derse geçin.
# END OF 07 - MOTOR POWER
# ============================================================