# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 07 - INPUT / OUTPUT
# ============================================================

# Input / Output (I/O), programın dışarıdan veri alması
# ve programdan dışarıya veri göndermesidir.
#
# Python'da:
#
# input()  -> kullanıcıdan veri alır
# print()  -> ekrana veri gönderir
#
# VEX'te ise input kavramı daha sonra Controller ve
# Sensor Library konularında genişleyecektir.


# ============================================================
# 01 - PRINT
# ============================================================

print("Hello World")

print(10)

print(10 + 20)

# print() verilen değeri ekrana yazdırır.


# ============================================================
# 02 - BİRDEN FAZLA DEĞER PRINT
# ============================================================

name = "Robot"

speed = 80

print(name, speed)

# Virgülle birden fazla değeri aynı anda yazdırabiliriz.
#
# Python bunların arasına otomatik olarak boşluk koyar.


# ============================================================
# 03 - TEXT VE NUMBER
# ============================================================

name = "VEX"

speed = 80

print("Robot:", name)
print("Speed:", speed)

# String ve number aynı print() içerisinde kullanılabilir.


# ============================================================
# 04 - F-STRING
# ============================================================

name = "VEX"

speed = 80

print(f"Robot: {name}")
print(f"Speed: {speed}")

# f-string, variable'ları text içerisinde
# kolayca kullanmamızı sağlar.
#
# f yazılır ve variable {} içerisine konur.


# ============================================================
# 05 - BİRDEN FAZLA VARIABLE İLE F-STRING
# ============================================================

left_speed = 50
right_speed = 70

print(f"Left: {left_speed}, Right: {right_speed}")

# Özellikle debug sırasında çok kullanışlıdır.


# ============================================================
# 06 - INPUT
# ============================================================

name = input("Name: ")

print(name)

# input() kullanıcıdan veri bekler.
#
# Kullanıcı Enter'a bastığında girilen değer
# variable'a kaydedilir.


# ============================================================
# 07 - INPUT HER ZAMAN STRING DÖNDÜRÜR
# ============================================================

age = input("Age: ")

print(type(age))

# Kullanıcı 15 yazsa bile input() sonucu:
#
# "15"
#
# yani string olur.


# ============================================================
# 08 - STRING'İ INTEGER'A ÇEVİRME
# ============================================================

age = input("Age: ")

age = int(age)

print(age)

print(type(age))

# int() string'i integer'a dönüştürür.


# ============================================================
# 09 - INPUT + INTEGER
# ============================================================

number = int(input("Number: "))

print(number + 10)

# Burada:
#
# input()
#     ↓
# string
#     ↓
# int()
#     ↓
# integer


# ============================================================
# 10 - FLOAT INPUT
# ============================================================

value = float(input("Value: "))

print(value)

# float() ondalıklı sayı oluşturur.
#
# Örneğin:
#
# "3.14" -> 3.14


# ============================================================
# 11 - INPUT İLE HESAPLAMA
# ============================================================

a = int(input("First number: "))

b = int(input("Second number: "))

result = a + b

print(f"Result: {result}")


# ============================================================
# 12 - STRING INPUT
# ============================================================

command = input("Command: ")

if command == "start":

    print("Starting")

elif command == "stop":

    print("Stopping")

else:

    print("Unknown command")


# String input'lar condition ile kontrol edilebilir.


# ============================================================
# 13 - INPUT + FUNCTION
# ============================================================

def square(number):

    return number * number


number = int(input("Number: "))

result = square(number)

print(result)

# Input'tan alınan veri function'a gönderilebilir.


# ============================================================
# 14 - INPUT + LIST
# ============================================================

numbers = []

number = int(input("Number: "))

numbers.append(number)

print(numbers)

# Input ile alınan değer listeye eklenebilir.


# ============================================================
# 15 - BİRDEN FAZLA INPUT
# ============================================================

name = input("Name: ")

team = input("Team: ")

print(f"Name: {name}")
print(f"Team: {team}")


# ============================================================
# 16 - OUTPUT OLARAK HESAPLAMA
# ============================================================

speed = 80

power = speed * 2

print(f"Speed: {speed}")
print(f"Power: {power}")


# ============================================================
# 17 - TYPE() İLE VERİ TÜRÜ KONTROLÜ
# ============================================================

number = 50

name = "VEX"

value = 3.14

print(type(number))
print(type(name))
print(type(value))

# type() bir variable'ın veri türünü gösterir.


# ============================================================
# 18 - STRING BİRLEŞTİRME
# ============================================================

first_name = "Yiğit"

last_name = "Robot"

full_name = first_name + " " + last_name

print(full_name)

# String'ler + operatörü ile birleştirilebilir.


# ============================================================
# 19 - STRING VE NUMBER HATASI
# ============================================================

number = 50

# Aşağıdaki kullanım hatalıdır:
#
# print("Speed: " + number)
#
# Çünkü string ile integer doğrudan + ile
# birleştirilemez.


# Doğru:

print("Speed: " + str(number))

# str() değeri string'e çevirir.


# ============================================================
# 20 - STR()
# ============================================================

number = 100

text = str(number)

print(text)

print(type(text))

# str() bir değeri string'e dönüştürür.


# ============================================================
# 21 - INT()
# ============================================================

text = "100"

number = int(text)

print(number)

print(type(number))


# ============================================================
# 22 - FLOAT()
# ============================================================

text = "12.5"

number = float(text)

print(number)

print(type(number))


# ============================================================
# 23 - KULLANICI GİRİŞİNİ KONTROL ETME
# ============================================================

number = int(input("Number: "))

if number > 0:

    print("Positive")

elif number < 0:

    print("Negative")

else:

    print("Zero")


# Input'tan gelen veri normal Python verisi gibi
# condition'larda kullanılabilir.


# ============================================================
# 24 - INPUT + WHILE
# ============================================================

command = ""

while command != "stop":

    command = input("Command: ")

    print(f"Received: {command}")

# Kullanıcı "stop" yazana kadar loop devam eder.


# ============================================================
# 25 - DEBUG OUTPUT
# ============================================================

speed = 75

error = 10

print(f"[DEBUG] speed={speed}")
print(f"[DEBUG] error={error}")

# Debug output robot programlarında çok önemlidir.
#
# Bir değerin beklediğimiz gibi olup olmadığını
# kontrol etmek için print() kullanabiliriz.


# ============================================================
# 26 - BİRDEN FAZLA DEĞERİ TEK PRINT'TE GÖSTERME
# ============================================================

left = 50
right = 60
error = 10

print(
    f"Left={left} | Right={right} | Error={error}"
)

# Özellikle robot hareket ederken birçok değeri
# aynı anda görmek için kullanışlıdır.


# ============================================================
# 27 - VEX BRAIN OUTPUT
# ============================================================

# VEX Brain ekranına veri yazdırmak için VEX API'sindeki
# Brain nesnesi kullanılır.
#
# Örneğin gerçek VEX projesinde:

from vex import *

brain = Brain()

brain.screen.print("Hello VEX")

# Burada:
#
# print()
#     Python konsoluna veri yazdırmak için kullanılır.
#
# brain.screen.print()
#     VEX Brain ekranına veri yazdırmak için kullanılır.


# ============================================================
# 28 - VEX BRAIN EKRANINDA VARIABLE
# ============================================================

speed = 80

brain.screen.print("Speed: %d" % speed)

# Brain ekranında robot verilerini göstermek,
# debug sırasında oldukça kullanışlıdır.


# ============================================================
# 29 - VEX'TE INPUT MANTIĞI
# ============================================================

# Python'daki:
#
# input()
#
# VEX robotunda genellikle joystick veya buton
# input'u anlamına gelmez.
#
# VEX'te controller input'ları Controller API'si
# üzerinden alınır.
#
# Örneğin gerçek bir VEX projesinde:

controller = Controller()

# Controller'ın buton ve joystick değerlerini daha sonra
# Controller Library bölümünde öğreneceğiz.


# ============================================================
# 30 - INPUT / OUTPUT KISA REFERANS
# ============================================================

# Kullanıcıdan veri:

name = input("Name: ")


# Integer input:

number = int(input("Number: "))


# Float input:

value = float(input("Value: "))


# String'e dönüştürme:

text = str(100)


# Integer'a dönüştürme:

number = int("100")


# Float'a dönüştürme:

number = float("3.14")


# Output:

print("Hello")


# F-string:

speed = 80

print(f"Speed: {speed}")


# VEX Brain output:

brain.screen.print("Hello VEX")


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# input()
#     Kullanıcıdan veri alır.
#
# ÖNEMLİ:
# input() sonucu her zaman string'dir.
#
# int()
#     Integer'a dönüştürür.
#
# float()
#     Ondalıklı sayıya dönüştürür.
#
# str()
#     String'e dönüştürür.
#
# print()
#     Python output'udur.
#
# f-string
#     Variable'ları text içerisinde kolayca göstermeyi sağlar.
#
# brain.screen.print()
#     VEX Brain ekranına output verir.
#
# VEX'te Controller ve Sensor input'ları ise
# kendi API'leri üzerinden alınır.
#
# Bu nedenle:
#
# input()
#     Python kullanıcı input'u
#
# Controller
#     Robot sürücüsünün input'u
#
# Sensor
#     Robotun çevreden aldığı input
#
# şeklinde düşünmek gerekir.





# ============================================================
# Ders 07 bitti, sıradaki derse geçebilirsiniz.
# END OF 07 - INPUT / OUTPUT
# ============================================================