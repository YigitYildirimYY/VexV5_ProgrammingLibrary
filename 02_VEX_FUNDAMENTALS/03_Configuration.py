# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 03 - CONFIGURATION
# ============================================================

from vex import *


# ============================================================
# 01 - CONFIGURATION NEDİR?
# ============================================================

# Configuration, robot üzerindeki cihazları programa
# tanıtma işlemidir.
#
# Örneğin robotumuzda:
#
#   PORT 1 -> Sol motor
#   PORT 2 -> Sağ motor
#   PORT 3 -> Inertial Sensor
#
# varsa Python programında da bu cihazları oluşturmalıyız.
#
# Önemli:
#
# Configuration sadece "hangi cihaz hangi portta?"
# sorusunu çözmez.
#
# Aynı zamanda motorun:
#
#   - Gear ratio
#   - Direction
#
# gibi temel ayarlarını da belirleyebiliriz.


# ============================================================
# 02 - MOTOR CONFIGURATION
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

# Motor oluştururken:
#
# Motor(
#     port,
#     gear_setting,
#     reversed
# )
#
# mantığını kullanıyoruz.
#
# PORT1:
#     Motorun bağlı olduğu port.
#
# RATIO_18_1:
#     Motor cartridge oranı.
#
# False / True:
#     Motor yönünün ters çevrilip çevrilmeyeceği.
#
# Özellikle sağ ve sol motorlarda direction ayarı
# önemlidir.


# ============================================================
# 03 - SENSOR CONFIGURATION
# ============================================================

inertial = Inertial(Ports.PORT3)

distance = Distance(Ports.PORT4)

rotation = Rotation(Ports.PORT5)

# Sensörlerde de aynı temel mantık vardır:
#
# DeviceType(Port)
#
# Örneğin:
#
#     Inertial(Ports.PORT3)
#     Distance(Ports.PORT4)
#     Rotation(Ports.PORT5)
#
# Daha sonra oluşturduğumuz isim üzerinden
# sensöre ulaşırız:
#
#     inertial
#     distance
#     rotation
#
# Sensörlerin özel ayarlarını ileride
# 04_SENSORS klasöründe detaylandıracağız.


# ============================================================
# 04 - MERKEZİ ROBOT CONFIGURATION
# ============================================================

# Büyük projelerde bütün cihazları programın
# başlangıcında toplamak çok daha düzenlidir.

brain = Brain()

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

inertial = Inertial(Ports.PORT3)

distance = Distance(Ports.PORT4)

# Böylece programın başında robotun donanımını
# açıkça görebiliriz.
#
# Daha sonra:
#
#     left_motor
#     right_motor
#     inertial
#     distance
#
# isimlerini kullanarak cihazlara erişiriz.
#
# Bu yaklaşım özellikle büyük robot projelerinde
# çok önemlidir.


# ============================================================
# 05 - CONFIGURATION'I AYRI TUTMAK
# ============================================================

# Configuration'ın temel amacı, robotun donanımı ile
# programın geri kalanını birbirinden ayırmaktır.
#
# Örneğin autonomous kodumuz:
#
#     left_motor.spin(...)
#
# diyebilir.
#
# Autonomous'un PORT1'in ne olduğunu bilmesine
# gerek yoktur.
#
# PORT1 bilgisi configuration kısmında tutulur.
#
# Böylece motoru PORT1'den PORT6'ya taşırsak:
#
#     left_motor = Motor(Ports.PORT6, ...)
#
# satırını değiştiririz.
#
# Robotun geri kalan kodunu değiştirmemiz gerekmez.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Configuration:
#     Robot üzerindeki cihazları programa tanıtma
#     ve temel ayarlarını belirleme işlemidir.
#
# Motor:
#
#     Motor(
#         Ports.PORT1,
#         GearSetting.RATIO_18_1,
#         False
#     )
#
# Sensor:
#
#     Distance(Ports.PORT4)
#
# Temel prensip:
#
#     Fiziksel cihaz
#          ↓
#     Python device
#          ↓
#     Programın geri kalanı
#
# Configuration'ı mümkün olduğunca merkezi tutmak,
# robotun donanımını değiştirdiğimizde kodu kolayca
# güncellememizi sağlar.
#
# İleride robotumuz büyüdüğünde bunu daha gelişmiş
# bir configuration sistemi haline getireceğiz.


# ============================================================
# Ders 03 bitti, sıradaki derse geçebilirsiniz.
# END OF 03 - CONFIGURATION
# ============================================================