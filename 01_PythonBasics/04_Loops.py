# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 04 - LOOPS
# ============================================================
#
# Loop = Bir kod bloğunu tekrar tekrar çalıştırmak.
#
# VEX'te looplar özellikle:
# - Driver Control
# - Sensor kontrolü
# - PID
# - Odometry
# - State Machine
# sistemlerinde kullanılır.
#
# ============================================================


# ============================================================
# 01 - WHILE
# ============================================================

# while, koşul True olduğu sürece çalışır.

number = 0

while number < 5:
    print(number)
    number += 1

# Çıktı:
# 0
# 1
# 2
# 3
# 4

# Mantık:
#
# koşulu kontrol et
#      ↓
# True -> kodu çalıştır
#      ↓
# tekrar koşulu kontrol et
#
# False olduğunda loop biter.


# ============================================================
# 02 - WHILE'DA EN ÖNEMLİ NOKTA
# ============================================================

counter = 0

while counter < 10:
    print(counter)
    counter += 1

# counter'ın değişmesi önemlidir.
#
# Aşağıdaki kod sonsuza kadar çalışır:
#
# counter = 0
# while counter < 10:
#     print(counter)
#
# Çünkü counter hiçbir zaman değişmez.


# ============================================================
# 03 - INFINITE LOOP
# ============================================================

# Robot programlarında sonsuz loop bazen bilinçli kullanılır.

while True:

    pass

# while True:
#     Her zaman True'dur.
#
# Robot çalıştığı sürece kontrol yapılması gereken
# durumlarda kullanılır.


# ============================================================
# 04 - BREAK
# ============================================================

# break loopu tamamen bitirir.

counter = 0

while True:

    print(counter)

    counter += 1

    if counter >= 5:
        break

# break çalıştığında loop sona erer.


# ============================================================
# 05 - BREAK KULLANIMI
# ============================================================

# Robot hedefe ulaşana kadar çalışabilir:

while True:

    # sensor_value = sensor.value()

    if sensor_value >= target:
        break

    # Robotu hareket ettir

# Mantık:
#
# Hedefe ulaşmadı -> devam et
# Hedefe ulaştı -> break


# ============================================================
# 06 - FOR
# ============================================================

# for belirli bir sequence üzerinde dolaşır.

for number in range(5):
    print(number)

# 0
# 1
# 2
# 3
# 4


# ============================================================
# 07 - RANGE
# ============================================================

# range(stop)

for i in range(5):
    print(i)

# 0, 1, 2, 3, 4
#
# ÖNEMLİ:
# stop değeri dahil değildir.


# range(start, stop)

for i in range(2, 6):
    print(i)

# 2, 3, 4, 5


# range(start, stop, step)

for i in range(0, 10, 2):
    print(i)

# 0, 2, 4, 6, 8


# ============================================================
# 08 - NEGATİF RANGE
# ============================================================

for i in range(5, 0, -1):
    print(i)

# 5, 4, 3, 2, 1


# ============================================================
# 09 - FOR + IF
# ============================================================

for number in range(10):

    if number % 2 == 0:
        print(number)

# Çift sayıları yazdırır.


# ============================================================
# 10 - CONTINUE
# ============================================================

# continue mevcut iteration'ı atlar.

for number in range(5):

    if number == 2:
        continue

    print(number)

# 0
# 1
# 3
# 4

# continue = Bu turu atla.
#
# break = Loopu tamamen bitir.


# ============================================================
# 11 - BREAK VS CONTINUE
# ============================================================

# break:

for i in range(10):

    if i == 5:
        break

    print(i)

# 0 1 2 3 4


# continue:

for i in range(10):

    if i == 5:
        continue

    print(i)

# 0 1 2 3 4 6 7 8 9


# ============================================================
# 12 - NESTED LOOP
# ============================================================

# Bir loopun içinde başka loop olabilir.

for row in range(3):

    for column in range(3):

        print(row, column)

# İç loop, dış loopun HER turunda baştan çalışır.


# ============================================================
# 13 - LOOP COUNTER
# ============================================================

counter = 0

for i in range(10):

    counter += 1

print(counter)

# counter = 10


# ============================================================
# 14 - ACCUMULATOR
# ============================================================

total = 0

for number in range(1, 6):

    total += number

print(total)

# 1 + 2 + 3 + 4 + 5 = 15


# ============================================================
# 15 - LISTE ÜZERİNDE LOOP
# ============================================================

motors = [
    "Left",
    "Right",
    "Intake"
]

for motor in motors:

    print(motor)

# for sadece sayılar için değildir.
# Listeler ve stringler üzerinde de kullanılabilir.


# ============================================================
# 16 - ENUMERATE
# ============================================================

motors = [
    "Left",
    "Right",
    "Intake"
]

for index, motor in enumerate(motors):

    print(index, motor)

# 0 Left
# 1 Right
# 2 Intake


# ============================================================
# 17 - HANGİSİNİ KULLANMALI?
# ============================================================

# Kaç kez çalışacağı belli:

for i in range(10):
    pass


# Bir koşul gerçekleşene kadar:

while sensor_value < target:
    pass


# Robot çalıştığı sürece:

while True:
    pass


# Belirli durumda tamamen çık:

while True:

    if condition:
        break


# ============================================================
# 18 - VEX LOOP MANTIĞI
# ============================================================

# Bir robot sürekli olarak:
#
# INPUT
#   ↓
# PROCESS
#   ↓
# OUTPUT
#
# yapar.

while True:

    # INPUT
    # Controller / Sensor oku

    # PROCESS
    # Hesaplama yap

    # OUTPUT
    # Motorları güncelle

    wait(20, MSEC)


# ============================================================
# 19 - DRIVER CONTROL
# ============================================================

# Basitleştirilmiş yapı:

while True:

    forward = controller_forward()
    turn = controller_turn()

    left = forward + turn
    right = forward - turn

    set_left_motor(left)
    set_right_motor(right)

    wait(20, MSEC)

# Her iteration:
#
# 1. Controller okunur.
# 2. Motor değerleri hesaplanır.
# 3. Motorlar güncellenir.
# 4. Loop tekrar başlar.


# ============================================================
# 20 - WAIT NEDEN KULLANILIR?
# ============================================================

while True:

    # Robot kontrolü

    wait(20, MSEC)

# wait loopun çok hızlı çalışmasını engeller.
#
# Kontrol sistemlerinde düzenli loop süresi önemlidir.
#
# Özellikle PID gibi sistemlerde loop timing önem kazanır.


# ============================================================
# 21 - SENSOR LOOP
# ============================================================

while True:

    distance = sensor_value

    if distance < 100:

        # Engel çok yakın

        stop_robot()

    else:

        drive_forward()

    wait(20, MSEC)


# ============================================================
# 22 - SENSOR İLE HEDEFE ULAŞMA
# ============================================================

while True:

    distance = sensor_value

    if distance <= target:

        stop_robot()
        break

    drive_forward()

    wait(20, MSEC)

# Hedefe ulaşınca:
#
# stop_robot()
# break
#
# çalışır ve loop sona erer.


# ============================================================
# 23 - AUTONOMOUS LOOP
# ============================================================

# Örneğin robot encoder ile hedefe ulaşana kadar ilerlesin:

while position < target_position:

    drive_forward()

    position = read_position()

    wait(10, MSEC)

stop_robot()

# Burada while:
# "Hedefe ulaşana kadar devam et"
# anlamına gelir.


# ============================================================
# 24 - PID LOOP
# ============================================================

# PID'nin ayrıntılarını ileride öğreneceğiz.
# Ancak temel yapı:

while True:

    sensor = read_sensor()

    error = target - sensor

    output = calculate_pid(error)

    set_motor(output)

    wait(20, MSEC)

# Her iteration yeni:
#
# sensor
# error
# output
#
# hesaplanır.


# ============================================================
# 25 - ODOMETRY LOOP
# ============================================================

# Odometry de sürekli güncellenebilir.

while True:

    left = read_left_encoder()
    right = read_right_encoder()

    update_position(left, right)

    wait(10, MSEC)

# Gerçek odometry çok daha karmaşıktır.
# Burada önemli olan sürekli güncelleme mantığıdır.


# ============================================================
# 26 - STATE MACHINE
# ============================================================

state = "DRIVE"

while True:

    if state == "DRIVE":

        drive()

    elif state == "INTAKE":

        intake()

    elif state == "SCORE":

        score()

    elif state == "STOP":

        stop()

        break

    wait(20, MSEC)

# Loop robotun mevcut state'ini sürekli kontrol eder.


# ============================================================
# 27 - LOOP + FUNCTION
# ============================================================

def update_drive():
    pass


def update_intake():
    pass


def update_sensors():
    pass


while True:

    update_drive()
    update_intake()
    update_sensors()

    wait(20, MSEC)

# Büyük projelerde loopun içine yüzlerce satır koymak yerine
# sistemleri fonksiyonlara ayırmak daha doğrudur.


# ============================================================
# 28 - LOOP İÇİNDE DEĞİŞKEN GÜNCELLEME
# ============================================================

speed = 0

while speed < 100:

    speed += 10

    set_motor(speed)

    wait(20, MSEC)

# Değişken her iteration'da güncellenir.


# ============================================================
# 29 - BİRDEN FAZLA DEĞİŞKEN
# ============================================================

speed = 0
distance = 0

while speed < 100:

    speed += 10
    distance += 20

    print(speed, distance)


# ============================================================
# 30 - AND / OR İLE LOOP
# ============================================================

speed = 0
distance = 0

while speed < 100 and distance < 500:

    speed += 10
    distance += 50


# and:
# Bütün koşullar True olmalı.


while speed < 100 or distance < 500:

    speed += 10
    distance += 50

# or:
# En az bir koşul True olduğu sürece devam eder.


# ============================================================
# 31 - LOOP'TA EN YAYGIN HATALAR
# ============================================================

# 1. Koşulu hiç değiştirmemek
#
# 2. Sonsuz loop oluşturmak
#
# 3. break ve continue'yu karıştırmak
#
# 4. range() stop değerini dahil sanmak
#
# 5. Gereksiz nested loop kullanmak
#
# 6. Robot loopuna wait koymamak
#
# 7. Büyük loopu fonksiyonlara ayırmamak


# ============================================================
# 32 - RANGE() ALTIN KURAL
# ============================================================

# range(start, stop, step)
#
# start -> dahil
# stop  -> DAHİL DEĞİL
# step  -> adım


for i in range(1, 5):
    print(i)

# 1 2 3 4


# ============================================================
# 33 - BREAK / CONTINUE ALTIN KURAL
# ============================================================

# break:
# LOOPU BİTİRİR.
#
# continue:
# SADECE BU TURU ATLAR.


# ============================================================
# 34 - WHILE / FOR ALTIN KURAL
# ============================================================

# Tekrar sayısı belliyse:

for i in range(10):
    pass


# Koşula bağlıysa:

while condition:
    pass


# Sürekli robot kontrolü:

while True:
    pass


# ============================================================
# 35 - GERÇEK VEX PROGRAMININ TEMELİ
# ============================================================

while True:

    # 1. INPUT

    # controller
    # sensors


    # 2. PROCESS

    # calculations
    # decisions


    # 3. OUTPUT

    # motors
    # mechanisms


    wait(20, MSEC)


# Bu yapı ileride:
#
# Driver Control
# PID
# Odometry
# State Machine
# Autonomous
#
# sistemlerinin temelini oluşturacak.


# ============================================================
# 36 - KISA REFERANS
# ============================================================

# while condition:
#     Koşul True olduğu sürece çalışır.


# for i in range(n):
#     Belirli sayıda tekrar.


# break
#     Loopu bitirir.


# continue
#     Mevcut iteration'ı atlar.


# range(start, stop, step)
#     Sayı aralığı oluşturur.


# while True:
#     Sonsuz loop.


# wait(20, MSEC)
#     VEX loop timing için kullanılır.


# ============================================================
# 37 - VEX İÇİN EN ÖNEMLİ 5 BİLGİ
# ============================================================
#
# 1. Robotun sürekli kontrol edilmesi gerekiyorsa while True.
#
# 2. Belirli sayıda tekrar gerekiyorsa for + range().
#
# 3. Hedefe ulaşınca çıkmak için break.
#
# 4. Bir iteration'ı atlamak için continue.
#
# 5. Sürekli çalışan robot looplarında wait kullan.




# ============================================================
# Ders 04 bitti, bir sonraki derse geçebilirsiniz.
# END OF 04 - LOOPS
# ============================================================