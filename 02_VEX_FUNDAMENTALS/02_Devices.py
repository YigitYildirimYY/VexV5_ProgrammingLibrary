# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 02 - DEVICES
# ============================================================

from vex import *


# ============================================================
# 01 - VEX DEVICE NEDİR?
# ============================================================

# VEX'te robot üzerinde kullandığımız elektronik parçaların
# büyük kısmı Python'da bir "device" olarak temsil edilir.
#
# Örneğin:
#
#     Brain
#     Motor
#     Controller
#     Inertial
#     Distance
#     Rotation
#     Optical
#
# Her device kendi class'ına sahiptir.
#
# Genel mantık:
#
#     device = DeviceType(port)
#
# Daha sonra device üzerinden o parçayı kontrol ederiz.


# ============================================================
# 02 - MOTOR BİR DEVICE'TIR
# ============================================================

brain = Brain()

motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)

# Burada üç önemli şey var:
#
# Motor(...)
#     Motor device'ı oluşturur.
#
# Ports.PORT1
#     Motorun Brain üzerinde bağlı olduğu port.
#
# GearSetting.RATIO_18_1
#     Motorun cartridge/gear oranı.
#
# False
#     Motorun reverse edilip edilmeyeceğini belirtir.
#
# Bundan sonra:
#
#     motor_1
#
# bizim Motor device'ımızdır.


# ============================================================
# 03 - BİRDEN FAZLA DEVICE OLUŞTURMA
# ============================================================

left_motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

right_motor = Motor(
    Ports.PORT2,
    GearSetting.RATIO_18_1,
    True
)

# Aynı device türünden birden fazla oluşturabiliriz.
#
# Burada iki farklı Motor device'ımız var:
#
#     left_motor
#     right_motor
#
# İkisi fiziksel olarak farklı portlardaki motorlardır.
#
# right_motor için True verdiğimiz için motorun yönünü
# yazılım seviyesinde ters çevirmiş olduk.


# ============================================================
# 04 - SENSOR DA BİR DEVICE'TIR
# ============================================================

inertial = Inertial(Ports.PORT3)

distance = Distance(Ports.PORT4)

# Burada da aynı temel mantık var:
#
#     Inertial(...)
#     Distance(...)
#
# ilgili device'ı oluşturur.
#
# Daha sonra bu device'ların kendi method ve
# özelliklerini kullanırız.
#
# Örneğin Distance sensor'dan veri almak:
#
#     distance.object_distance(MM)
#
# şeklinde yapılabilir.
#
# Sensörlerin detaylarını 04_SENSORS klasöründe
# ayrı ayrı inceleyeceğiz.


# ============================================================
# 05 - DEVICE'I KULLANMA MANTIĞI
# ============================================================

motor = Motor(
    Ports.PORT5,
    GearSetting.RATIO_18_1,
    False
)

motor.set_velocity(50, PERCENT)

motor.spin(FORWARD)

wait(1, SECONDS)

motor.stop()

# Burada önemli olan device mantığını anlamaktır:
#
# 1. Device oluşturduk:
#
#     motor = Motor(...)
#
# 2. Device'ın ayarını değiştirdik:
#
#     motor.set_velocity(...)
#
# 3. Device'a komut verdik:
#
#     motor.spin(...)
#
# 4. Device'ı durdurduk:
#
#     motor.stop()
#
# İleride kullanacağımız bütün VEX cihazlarında
# temel mantık büyük ölçüde buna dayanır.
#
#
# ============================================================
# ANAHTAR BİLGİLER
# ============================================================
#
# Device:
#     Robot üzerindeki programlanabilir elektronik parçanın
#     Python'daki temsilidir.
#
# Motor:
#     Motor device'ı.
#
# Controller:
#     Controller device'ı.
#
# Sensor:
#     Sensör device'ı.
#
# Ports.PORT1:
#     Device'ın bağlı olduğu Brain portunu belirtir.
#
# Device oluşturma:
#
#     motor = Motor(...)
#     inertial = Inertial(...)
#
# Device kullanma:
#
#     motor.spin(...)
#     motor.stop(...)
#     distance.object_distance(...)
#
# En önemli fikir:
#
# Python'da fiziksel parçayı doğrudan kontrol etmiyoruz.
# Önce o parçanın Python'daki device nesnesini oluşturuyor,
# sonra o nesnenin methodlarını kullanıyoruz.
# KARTUŞ ORANLARI EKLENECEK MAVİ KIRMIZI YEŞİL
# ============================================================
# Ders 02 bitti, sıradaki derse geçebilirsiniz.
# END OF 02 - DEVICES
# ============================================================
