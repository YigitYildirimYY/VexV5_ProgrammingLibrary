# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 05 - MOTOR TORQUE
# ============================================================

from vex import *


# ============================================================
# 01 - TORQUE NEDİR?
# ============================================================

# Torque (tork), motorun döndürme kuvvetini ifade eder.
#
# Basitçe:
#
#     Velocity → Ne kadar hızlı dönüyor?
#     Torque   → Ne kadar döndürme kuvveti uyguluyor?
#
# Özellikle:
#
#     Lift
#     Arm
#     Intake
#     Ağır mekanizmalar
#
# gibi sistemlerde tork önemli bir değerdir.
#
# VEX Smart Motor'da mevcut tork değerini okuyabiliriz.
#
# Tork sınırını ayarlamak için ise:
#
#     set_max_torque()
#
# kullanılır.
#
# Bu dosyada öncelikle mevcut tork değerini
# okumaya odaklanacağız.


motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)


# ============================================================
# 02 - TORQUE OKUMA
# ============================================================

motor.spin(FORWARD, 50, PERCENT)

wait(500, MSEC)

torque = motor.torque(TorqueUnits.NM)

print(torque)

motor.stop()

# torque() motorun o anda kullandığı torku döndürür.
#
# TorqueUnits.NM:
#     Newton-metre cinsinden tork.
#
# Örneğin:
#
#     motor.torque(TorqueUnits.NM)
#
# motorun torkunu Newton-metre olarak verir.
#
# VEX Python API'de torque() için kullanılabilen
# birimler:
#
#     TorqueUnits.NM
#     TorqueUnits.INLB
#
# PERCENT burada kullanılamaz.


# ============================================================
# 03 - INCH-POUND OLARAK TORQUE OKUMA
# ============================================================

motor.spin(FORWARD, 50, PERCENT)

wait(500, MSEC)

torque_inlb = motor.torque(TorqueUnits.INLB)

print(torque_inlb)

motor.stop()

# TorqueUnits.INLB:
#
#     Torku inch-pound cinsinden verir.
#
# Böylece aynı motor torkunu iki farklı fiziksel
# birimde okuyabiliriz:
#
#     TorqueUnits.NM
#     TorqueUnits.INLB


# ============================================================
# 04 - TORQUE NEDEN ÖNEMLİ?
# ============================================================

# Bir mekanizma ağır yük altında çalışıyorsa motorun
# daha fazla tork üretmesi gerekebilir.
#
# Örneğin bir lift:
#
#     Hafif yük
#          ↓
#     Daha düşük tork ihtiyacı
#
#     Ağır yük
#          ↓
#     Daha yüksek tork ihtiyacı
#
# Motorun zorlandığı durumlarda:
#
#     Torque
#     Current
#     Temperature
#
# gibi değerleri incelemek robotu debug ederken
# faydalı olabilir.
#
# Ancak motorun daha yüksek tork kullanması,
# mekanik sistemin otomatik olarak daha güçlü olduğu
# anlamına gelmez.
#
# Gear ratio, motor sayısı ve mekanik avantaj gibi
# faktörler de önemlidir.


# ============================================================
# 05 - MAXIMUM TORQUE AYARLAMA
# ============================================================

# Motorun kullanabileceği maksimum torku sınırlamak
# için set_max_torque() kullanılabilir.
#
# Örneğin:

motor.set_max_torque(
    50,
    PERCENT
)

# Burada:
#
#     50 PERCENT
#
# motorun kullanabileceği maksimum torku sınırlar.
#
# Bu, torque() ile aynı şey değildir.
#
# torque():
#     Mevcut kullanılan torku OKUR.
#
# set_max_torque():
#     Kullanılabilecek maksimum torku AYARLAR.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Mevcut torku oku:
#
#     motor.torque(TorqueUnits.NM)
#
#
# Inch-pound olarak oku:
#
#     motor.torque(TorqueUnits.INLB)
#
#
# Maksimum torku sınırla:
#
#     motor.set_max_torque(50, PERCENT)
#
#
# Önemli ayrım:
#
#     torque()
#         → Mevcut torku okur.
#
#     set_max_torque()
#         → Maksimum torku ayarlar.
#
#
# Torque:
#     Motorun döndürme kuvvetiyle ilgili bir ölçüdür.
#
# Velocity:
#     Motorun dönüş hızını ifade eder.
#
#
# VEX Python'da torque() için geçerli birimler:
#
#     TorqueUnits.NM
#     TorqueUnits.INLB
#
# PERCENT:
#     torque() okumada kullanılmaz.
#     set_max_torque() ile maksimum tork sınırı
#     belirlerken kullanılabilir.


# ============================================================
# Ders 05 bitti, bir sonraki derse geçin.
# END OF 05 - MOTOR TORQUE
# ============================================================