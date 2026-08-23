# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 01 - MOTOR BASICS
# ============================================================

from vex import *


# ============================================================
# 01 - MOTOR NEDİR?
# ============================================================

# VEX V5 Motor, robotun mekanik parçalarını hareket
# ettirmek için kullandığımız temel cihazdır.
#
# Örneğin:
#
#     Drivetrain
#     Intake
#     Arm
#     Lift
#     Conveyor
#
# gibi sistemlerde motor kullanabiliriz.
#
# Python'da önce motoru programa tanıtırız.


motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

# Motor() oluştururken temel olarak:
#
#     Motor(
#         PORT,
#         GEAR_SETTING,
#         REVERSED
#     )
#
# kullanıyoruz.
#
# PORT:
#     Motorun Brain üzerinde bağlı olduğu port.
#
# GEAR_SETTING:
#     Motorun cartridge oranı.
#
# REVERSED:
#     Motor yönünün ters çevrilip çevrilmeyeceği.


# ============================================================
# 02 - MOTOR PORT
# ============================================================

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

# Burada motor PORT1'e bağlıdır.
#
# Eğer motoru fiziksel olarak PORT6'ya taşırsak:
#
#     Ports.PORT1
#
# yerine:
#
#     Ports.PORT6
#
# yazmamız gerekir.
#
# Önemli:
#
# Python'daki PORT numarası ile motorun fiziksel olarak
# bağlandığı Brain portu aynı olmalıdır.
#
# Yanlış port kullanırsak program başka bir motoru
# kontrol etmeye çalışabilir veya cihaz bulunamayabilir.


# ============================================================
# 03 - GEAR SETTING
# ============================================================

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

# VEX V5 Smart Motor farklı cartridge oranlarıyla
# kullanılabilir.
#
# Örneğin:
#
#     GearSetting.RATIO_36_1
#     GearSetting.RATIO_18_1
#     GearSetting.RATIO_6_1
#
# Bu değer motorun kullanılan gear cartridge'ını
# programa bildirir.
#
# Bu ayar sadece "motorun hızlı mı yavaş mı çalışacağını"
# seçmek değildir.
#
# Motorun ölçüm ve kontrol davranışlarının doğru olması
# açısından da doğru gear setting kullanmak önemlidir.
#
# Fiziksel olarak hangi cartridge takılıysa kodda
# ona uygun setting kullanılmalıdır.


# ============================================================
# 04 - REVERSED
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

# İki motor fiziksel olarak aynı yöne dönüyor gibi görünse
# bile robot üzerindeki yerleşimleri nedeniyle bir tarafın
# ters yönde kontrol edilmesi gerekebilir.
#
# Bunun için:
#
#     False
#
# veya:
#
#     True
#
# kullanabiliriz.
#
# Örneğin tank drivetrain:
#
#     left_motor  -> False
#     right_motor -> True
#
# şeklinde olabilir.
#
# Böylece iki motora da:
#
#     spin(FORWARD)
#
# dediğimizde robotun iki tarafı da robot açısından
# ileri yönde hareket edebilir.


# ============================================================
# 05 - MOTOR NESNESİNİN TEMEL MANTIĞI
# ============================================================

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

# Artık "motor" isminde bir Motor nesnemiz var.
#
# Motorun kendisini değil, oluşturduğumuz nesneyi
# kullanarak motora komut veririz.
#
# Örneğin:
#
#     motor.spin(...)
#     motor.stop()
#     motor.set_velocity(...)
#
# gibi komutlar ilerleyen dosyalarda kullanılacak.
#
# Bu nedenle:
#
#     motor
#
# sadece bir variable gibi görünse de aslında
# VEX Motor nesnesini temsil eder.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Motor oluşturmanın temel şekli:
#
#     motor = Motor(
#         Ports.PORT1,
#         GearSetting.RATIO_18_1,
#         False
#     )
#
#
# Üç temel bilgi:
#
#     1. PORT
#     2. GEAR SETTING
#     3. REVERSED
#
#
# PORT:
#     Motorun fiziksel bağlantı noktası.
#
# GEAR SETTING:
#     Kullanılan motor cartridge oranı.
#
# REVERSED:
#     Motorun kontrol yönünü tersine çevirir.
#
#
# Önemli:
#
# Configuration bölümünde oluşturduğumuz motor
# nesneleri daha sonra bütün robot kodu tarafından
# kullanılabilir.
#
# Örneğin:
#
#     left_motor
#     right_motor
#     intake_motor
#     lift_motor
#
# gibi isimlendirmeler kullanmak, büyük robot
# projelerinde kodun okunabilirliğini ciddi şekilde artırır.
#
# Bir sonraki dosyada artık motoru oluşturmakla kalmayıp
# ona gerçek hareket komutları göndermeye başlayacağız:
#
#     spin()
#     stop()
#     spin_for()
#     spin_to_position()



# ============================================================
# Ders 01 bitti, bir sonraki derse geçin.
# END OF 01 - MOTOR BASICS
# ============================================================