from vex import *

# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 01 - VARIABLES
# ============================================================


# ------------------------------------------------------------
# 1. DEĞİŞKEN NEDİR?
# ------------------------------------------------------------
#
# Değişken, program içerisinde bir değeri saklamak için
# kullandığımız isimlendirilmiş alandır.
#
# Genel kullanım:
#
#     variable = value
#
# Örnek:

speed = 50

# Artık "speed" değişkeninin değeri 50'dir.
#
# Bu değeri daha sonra programın herhangi bir yerinde
# kullanabiliriz:

print(speed)

# Değişkenin değeri sonradan değiştirilebilir:

speed = 80

print(speed)

# Artık speed = 80'dir.


# ------------------------------------------------------------
# 2. INTEGER (int)
# ------------------------------------------------------------
#
# Integer tam sayıdır.
#
# VEX programlamada:
# - motor hızları
# - mesafeler
# - açı değerleri
# - sayaçlar
# gibi değerlerde kullanılabilir.

drive_speed = 80
target_distance = 1000
target_heading = 90
counter = 0

print(drive_speed)
print(target_distance)


# ------------------------------------------------------------
# 3. FLOAT
# ------------------------------------------------------------
#
# Float ondalıklı sayıdır.
#
# Özellikle:
# - PID katsayıları
# - robot koordinatları
# - sensör hesaplamaları
# - odometry
# gibi sistemlerde kullanılır.

kp = 0.35
wheel_diameter = 2.75
robot_x = 125.73
robot_y = 438.21

print(kp)
print(robot_x)


# ------------------------------------------------------------
# 4. BOOLEAN (bool)
# ------------------------------------------------------------
#
# Boolean sadece iki değer alabilir:
#
# True
# False
#
# Robotun bir durumunu takip etmek için çok kullanışlıdır.

robot_ready = True
intake_running = False
autonomous_finished = False

print(robot_ready)
print(intake_running)


# ------------------------------------------------------------
# 5. STRING (str)
# ------------------------------------------------------------
#
# String metin saklar.
#
# Tırnak içerisinde yazılır.

robot_name = "High Skates"
team_name = "Elegance Robotics"
status = "READY"

print(robot_name)
print(team_name)
print(status)


# ------------------------------------------------------------
# 6. DEĞİŞKENLERLE MATEMATİK
# ------------------------------------------------------------

speed = 50
boost = 20

final_speed = speed + boost

print(final_speed)

# final_speed = 70


# ------------------------------------------------------------
# 7. MOTOR HIZI HESAPLAMA
# ------------------------------------------------------------
#
# Sabit bir sayı yazmak yerine değişken kullanmak,
# robotun ayarlarını değiştirmeyi kolaylaştırır.

MAX_SPEED = 100
AUTON_SPEED_PERCENT = 0.70

auton_speed = MAX_SPEED * AUTON_SPEED_PERCENT

print(auton_speed)

# Sonuç:
# auton_speed = 70


# ------------------------------------------------------------
# 8. VEX MOTOR İLE KULLANIM
# ------------------------------------------------------------

brain = Brain()

drive_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)

DRIVE_SPEED = 50

drive_motor.set_velocity(DRIVE_SPEED, PERCENT)
drive_motor.spin(FORWARD)

wait(2, SECONDS)

drive_motor.stop()


# ------------------------------------------------------------
# 9. DEĞİŞKENLERİ GÜNCELLEME
# ------------------------------------------------------------

counter = 0

counter = counter + 1
print(counter)

counter = counter + 1
print(counter)

# Daha kısa yazımı:

counter += 1

# Şimdi counter = 3


# Diğer kısa yazımlar:

speed = 100

speed -= 10
# speed = 90

speed *= 2
# speed = 180

speed /= 2
# speed = 90


# ------------------------------------------------------------
# 10. SENSOR DEĞERİNİ DEĞİŞKENE KAYDETME
# ------------------------------------------------------------
#
# Sensörden gelen değeri doğrudan kullanmak yerine
# çoğu zaman bir değişkene kaydetmek daha kullanışlıdır.
#
# Örneğin bir rotation sensor:

rotation_sensor = Rotation(
    Ports.PORT2,
    False
)

current_position = rotation_sensor.position(DEGREES)

print(current_position)


# ------------------------------------------------------------
# 11. TARGET - CURRENT = ERROR
# ------------------------------------------------------------
#
# Bu yapı VEX'teki kontrol sistemlerinin temelidir.
#
# Robotun ulaşmasını istediğimiz değer TARGET,
# robotun şu anki değeri CURRENT,
# aralarındaki fark ise ERROR'dur.

target_position = 180
current_position = 150

error = target_position - current_position

print(error)

# error = 30


# ------------------------------------------------------------
# 12. HEADING ERROR
# ------------------------------------------------------------

target_heading = 90
current_heading = 72

heading_error = target_heading - current_heading

print(heading_error)

# heading_error = 18


# ------------------------------------------------------------
# 13. SABİTLER
# ------------------------------------------------------------
#
# Python'da gerçek anlamda "constant" bulunmaz.
# Ancak değişmemesi gereken değerleri büyük harfle
# yazmak standart bir kullanımdır.

WHEEL_DIAMETER = 2.75
TRACK_WIDTH = 12.5

MAX_DRIVE_SPEED = 100
TURN_SPEED = 60
INTAKE_SPEED = 100


# ------------------------------------------------------------
# 14. PID AYARLARINI DEĞİŞKEN OLARAK SAKLAMA
# ------------------------------------------------------------
#
# PID'ye sonraki aşamalarda değineceğiz,
# Sadece PID'nin kullanacağı değerleri saklıyoruz

DRIVE_KP = 0.25
DRIVE_KI = 0.00
DRIVE_KD = 0.15

TURN_KP = 0.35
TURN_KI = 0.00
TURN_KD = 0.20


# ------------------------------------------------------------
# 15. BİR ROBOT CONFIGURATION ÖRNEĞİ
# ------------------------------------------------------------

# Robot fiziksel özellikleri
WHEEL_DIAMETER = 2.75
TRACK_WIDTH = 12.5

# Drive
DRIVE_SPEED = 80
TURN_SPEED = 60

# Mechanisms
INTAKE_SPEED = 100
ARM_SPEED = 70

# Drive PID
DRIVE_KP = 0.25
DRIVE_KI = 0.00
DRIVE_KD = 0.15

# Turn PID
TURN_KP = 0.35
TURN_KI = 0.00
TURN_KD = 0.20


# ------------------------------------------------------------
# 16. TYPE()
# ------------------------------------------------------------
#
# Bir değişkenin veri tipini görmek için type() kullanılır.

speed = 80
kp = 0.35
robot_ready = True
robot_name = "High Skates"

print(type(speed))
print(type(kp))
print(type(robot_ready))
print(type(robot_name))

# Çıktılar:
#
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'str'>


# ------------------------------------------------------------
# 17. DEĞİŞKEN İSİMLENDİRME
# ------------------------------------------------------------
#
# Python'da okunabilir isimler kullanmak önemlidir.
#
# KÖTÜ:

x = 80
y = 60
z = 100

# Bunların ne olduğu belli değil
#
# DAHA İYİ:

drive_speed = 80
turn_speed = 60
intake_speed = 100


# ------------------------------------------------------------
# 18. SNAKE_CASE
# ------------------------------------------------------------
#
# Bu kütüphanede Python değişkenleri için snake_case
# kullanacağız.
#
# Kelimeler "_" ile ayrılır.

target_distance = 1000
target_heading = 90
current_velocity = 50
previous_error = 10


# ------------------------------------------------------------
# 19. BÜYÜK HARFLE SABİTLER
# ------------------------------------------------------------
#
# Program boyunca değiştirmememiz gereken ayarlar
# büyük harfle yazılacak.

MAX_SPEED = 100
WHEEL_DIAMETER = 2.75
TRACK_WIDTH = 12.5


# ------------------------------------------------------------
# 20. VEX PROGRAMLAMA İÇİN ÖNEMLİ DEĞİŞKENLER
# ------------------------------------------------------------
#
# İleride yazacağımız sistemlerde buna benzer değişkenler
# sürekli kullanılacak.

robot_x = 0.0
robot_y = 0.0
robot_heading = 0.0

target_x = 1000.0
target_y = 500.0
target_heading = 90.0

current_velocity = 0.0
target_velocity = 100.0

error = 0.0
previous_error = 0.0
integral = 0.0
derivative = 0.0
output = 0.0


# ------------------------------------------------------------
# 21. DEĞİŞKENLERLE BASİT PID MANTIĞI
# ------------------------------------------------------------
#
# Henüz gerçek bir PID class'ı yazmıyoruz.
# Burada yalnızca değişkenlerin nasıl kullanıldığını
# görüyoruz.

target = 100
current = 70

error = target - current

kp = 0.5

output = kp * error

print(output)

# error = 30
# output = 15


# ------------------------------------------------------------
# 22. DEĞİŞKENLERİ BİRLEŞTİRME
# ------------------------------------------------------------

base_speed = 50
correction = 10

left_speed = base_speed + correction
right_speed = base_speed - correction

print(left_speed)
print(right_speed)

# Bu mantık ileride PID ile:
#
# left_speed  = base_speed + turn_correction
# right_speed = base_speed - turn_correction
#
# şeklinde kullanılacaktır.


# ------------------------------------------------------------
# 23. DEĞİŞKENLERLE ROBOT DURUMU
# ------------------------------------------------------------

robot_ready = False
autonomous_running = False
intake_running = False

# Robot başlatıldığında:

robot_ready = True

# Autonomous başladığında:

autonomous_running = True

# Intake başladığında:

intake_running = True

print(robot_ready)
print(autonomous_running)
print(intake_running)


# ------------------------------------------------------------
# 24. DEĞİŞKENLERİN ÖNEMİ
# ------------------------------------------------------------
#
# VEX programlamada ileride yazacağımız:
#
# PID
# Odometry
# Pure Pursuit
# Motion Profiling
# State Machine
# Autonomous
# Telemetry
#
# sistemlerinin tamamı değişkenler üzerine kurulacaktır.
#
# Örneğin odometry:

x = 0.0
y = 0.0
heading = 0.0

# PID:

error = 0.0
previous_error = 0.0
integral = 0.0
derivative = 0.0

# Motion profiling:

target_velocity = 0.0
current_velocity = 0.0
acceleration = 0.0

# Pure Pursuit:

lookahead_distance = 200.0
target_x = 0.0
target_y = 0.0




# ============================================================
# Ders01 bitti, bir sonraki dersten devam edebilirsiniz.
# END OF VARIABLES
# ============================================================
