# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 08 - MODULES
# ============================================================

# Module, Python kodlarını başka bir .py dosyasından
# kullanmamızı sağlayan yapıdır.
#
# Büyük projelerde bütün kodu tek dosyada tutmak yerine
# farklı dosyalara bölmek için kullanılır.
#
# Örneğin:
#
# main.py
# motors.py
# sensors.py
# autonomous.py
#
# şeklinde bir proje oluşturabiliriz.


# ============================================================
# 01 - MODULE NEDİR?
# ============================================================

# Her .py dosyası temel olarak bir Python module'üdür.
#
# Örneğin:
#
# math_tools.py
#
# adlı bir dosyamız varsa bu dosyayı başka bir Python
# dosyasından module olarak kullanabiliriz.


# ============================================================
# 02 - IMPORT
# ============================================================

import math

print(math.sqrt(25))

# import math
#
# math module'ünü programa dahil eder.
#
# sqrt() fonksiyonuna:
#
# math.sqrt()
#
# şeklinde ulaşırız.


# ============================================================
# 03 - MODULE İÇERİSİNDEKİ FONKSİYONA ULAŞMA
# ============================================================

import math

number = math.sqrt(100)

print(number)

# Module adı + "." + fonksiyon adı
#
# şeklinde kullanılır.


# ============================================================
# 04 - CONSTANT DEĞERLERE ULAŞMA
# ============================================================

import math

print(math.pi)

# math module'ünün içerisindeki pi değerine
# math.pi şeklinde ulaşabiliriz.


# ============================================================
# 05 - IMPORT AS
# ============================================================

import math as m

print(m.sqrt(16))

# as ile module'e farklı bir isim verebiliriz.
#
# math yerine m kullandık.


# ============================================================
# 06 - FROM IMPORT
# ============================================================

from math import sqrt

print(sqrt(25))

# Böylece sqrt() fonksiyonunu doğrudan kullanabiliriz.
#
# math.sqrt()
# yerine:
#
# sqrt()
#
# yazılır.


# ============================================================
# 07 - BİRDEN FAZLA DEĞER IMPORT ETME
# ============================================================

from math import sqrt, pi

print(sqrt(36))
print(pi)

# Bir module'den birden fazla öğe import edilebilir.


# ============================================================
# 08 - FROM MODULE IMPORT *
# ============================================================

# Örneğin:
#
# from math import *
#
# module içerisindeki birçok öğeyi doğrudan kullanmamızı
# sağlar.
#
# Ancak büyük projelerde bu yöntem genellikle önerilmez.
#
# Çünkü hangi fonksiyonun hangi module'den geldiğini
# anlamak zorlaşabilir.


# ============================================================
# 09 - KENDİ MODULE'ÜMÜZÜ OLUŞTURMA
# ============================================================

# Örneğin aynı klasörde:
#
# calculations.py
#
# adlı bir dosyamız olduğunu düşünelim.
#
# İçeriği:
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
# olabilir.


# ============================================================
# 10 - KENDİ MODULE'ÜMÜZÜ IMPORT ETME
# ============================================================

# calculations.py dosyası varsa:
#
# import calculations
#
# şeklinde import edebiliriz.
#
# Daha sonra:
#
# calculations.add(5, 3)
#
# calculations.multiply(5, 3)
#
# şeklinde kullanabiliriz.


# ============================================================
# 11 - MODULE İÇERİSİNDEKİ FUNCTION
# ============================================================

# calculations.py:
#
# def add(a, b):
#
#     return a + b
#
#
# main.py:
#
# import calculations
#
# result = calculations.add(10, 20)
#
# print(result)


# ============================================================
# 12 - FROM KULLANARAK KENDİ MODULE'ÜMÜZ
# ============================================================

# calculations.py:
#
# def add(a, b):
#     return a + b
#
#
# main.py:
#
# from calculations import add
#
# result = add(10, 20)
#
# print(result)


# ============================================================
# 13 - MODULE'E ALIAS VERME
# ============================================================

# Örneğin:
#
# import calculations as calc
#
# result = calc.add(10, 20)
#
# print(result)
#
# calc artık calculations module'ünün kısa ismidir.


# ============================================================
# 14 - MODULE İÇİNDE VARIABLE
# ============================================================

# robot_settings.py:
#
# max_speed = 100
# default_speed = 50
#
#
# main.py:
#
# import robot_settings
#
# print(robot_settings.max_speed)
# print(robot_settings.default_speed)


# ============================================================
# 15 - MODULE İÇERİSİNDE FUNCTION + VARIABLE
# ============================================================

# robot_settings.py:
#
# max_speed = 100
#
#
# def limit_speed(speed):
#
#     if speed > max_speed:
#         return max_speed
#
#     return speed
#
#
# main.py:
#
# import robot_settings
#
# print(robot_settings.limit_speed(150))


# ============================================================
# 16 - MODULE'ÜN BİR KEZ YÜKLENMESİ
# ============================================================

# Bir module import edildiğinde Python onu yükler.
#
# Aynı module'ü tekrar import etmek normalde yeniden
# ayrı bir module oluşturmaz.
#
# Bu nedenle module'ler kodun ortak parçalarını
# paylaşmak için kullanılabilir.


# ============================================================
# 17 - __NAME__
# ============================================================

# Python'da özel bir variable vardır:
#
# __name__
#
# Bir dosya doğrudan çalıştırıldığında:
#
# __name__ == "__main__"
#
# olur.


# ============================================================
# 18 - IF __NAME__
# ============================================================

if __name__ == "__main__":

    print("This file is running directly")

# Bu yapı özellikle module'lerde çok önemlidir.
#
# Dosya doğrudan çalıştırılırsa içindeki kod çalışır.
#
# Başka bir dosyadan import edilirse bu bölüm
# otomatik olarak çalışmaz.


# ============================================================
# 19 - NEDEN __NAME__ KULLANILIR?
# ============================================================

# Örneğin:
#
# calculations.py
#
# içerisinde:
#
# def add(a, b):
#     return a + b
#
#
# if __name__ == "__main__":
#
#     print(add(5, 3))
#
#
# calculations.py doğrudan çalıştırılırsa:
#
# 8
#
# yazdırılır.
#
# Ama başka bir dosya:
#
# import calculations
#
# dediğinde print() çalışmaz.


# ============================================================
# 20 - VEX MODÜLÜ
# ============================================================

# VEX Python API'sini kullanmak için:
#
# from vex import *
#
# kullanılır.
#
# VEXcode tarafından oluşturulan projelerde bu yapı
# sıkça görülür.


# ============================================================
# 21 - VEX MODÜLÜNDEN ÖĞELER
# ============================================================

# from vex import *
#
# ile VEX API'sindeki:
#
# Brain
# Motor
# Controller
# Inertial
# Distance
# Rotation
# Optical
#
# gibi sınıflara erişebiliriz.
#
# Ancak gerçek cihazları burada tanımlamıyoruz.
# Cihaz tanımları ilgili VEX projelerinde yapılmalıdır.


# ============================================================
# 22 - KÜTÜPHANEYİ DOSYALARA BÖLME
# ============================================================

# Büyük bir VEX projesini örneğin:
#
# main.py
# motors.py
# sensors.py
# pid.py
# autonomous.py
#
# şeklinde ayırabiliriz.
#
# main.py ana programı yönetir.
#
# motors.py motor functionlarını içerir.
#
# sensors.py sensör işlemlerini içerir.
#
# pid.py PID hesaplamalarını içerir.
#
# autonomous.py autonomous rutinlerini içerir.


# ============================================================
# 23 - MOTOR MODULE ÖRNEĞİ
# ============================================================

# motors.py:
#
# def drive(speed):
#
#     # motor kodları
#     pass
#
#
# def stop():
#
#     # motor stop kodları
#     pass
#
#
# main.py:
#
# import motors
#
# motors.drive(50)
# motors.stop()


# ============================================================
# 24 - SENSOR MODULE ÖRNEĞİ
# ============================================================

# sensors.py:
#
# def get_distance():
#
#     # gerçek sensör okuma kodu
#     return 100
#
#
# main.py:
#
# import sensors
#
# distance = sensors.get_distance()
#
# print(distance)
#
# Böylece main.py sensörün nasıl çalıştığını bilmek
# zorunda kalmaz.


# ============================================================
# 25 - MODULE'LERİN BİRBİRİNİ KULLANMASI
# ============================================================

# Örneğin:
#
# pid.py
#     ↓
# sensors.py
#
# veya:
#
# autonomous.py
#     ↓
# motors.py
#     ↓
# sensors.py
#
# şeklinde module'ler birbirinden yararlanabilir.
#
# Bu yapı büyük robot projelerinin temel mimarisidir.


# ============================================================
# 26 - MODULE İSİMLERİNDE DİKKAT
# ============================================================

# Module isimleri:
#
# motors.py
# sensors.py
# pid.py
# autonomous.py
#
# gibi kısa ve açıklayıcı olmalıdır.
#
# Boşluk kullanmamak gerekir.
#
# Kötü:
#
# robot motors.py
#
# İyi:
#
# robot_motors.py


# ============================================================
# 27 - AYNI İSİMLİ DOSYALARA DİKKAT
# ============================================================

# Örneğin kendi dosyamıza:
#
# math.py
#
# adını vermek kötü bir fikirdir.
#
# Çünkü Python'un gerçek math module'ü ile
# karışıklık oluşturabilir.
#
# Aynı şekilde:
#
# random.py
# time.py
#
# gibi standart module isimlerini de kendi dosyalarımız
# için kullanmamak daha güvenlidir.


# ============================================================
# 28 - MODULE VE KÜTÜPHANE ARASINDAKİ FARK
# ============================================================

# Module:
#     Tek bir .py dosyasıdır.
#
# Library:
#     Bir veya daha fazla module'den oluşan
#     kullanılabilir kod topluluğudur.
#
# Örneğin bizim VEX kütüphanemiz:
#
# motors.py
# sensors.py
# pid.py
# odometry.py
#
# gibi birçok module içerebilir.


# ============================================================
# 29 - VEX KÜTÜPHANEMİZDE MODÜLER YAPI
# ============================================================

# İleride oluşturacağımız yapı yaklaşık olarak:
#
# VEX_Library/
#
#     main.py
#
#     motors.py
#     sensors.py
#     drivetrain.py
#     pid.py
#     odometry.py
#     autonomous.py
#
# şeklinde olabilir.
#
# main.py:
#
# import drivetrain
# import autonomous
#
# drivetrain.drive()
# autonomous.run()
#
# gibi çalışabilir.


# ============================================================
# 30 - MODULE KISA REFERANS
# ============================================================

# Module import:

import math


# Module içindeki function:

math.sqrt(25)


# Alias:

import math as m

m.sqrt(25)


# Belirli function import:

from math import sqrt

sqrt(25)


# Birden fazla öğe:

from math import sqrt, pi # type: ignore


# Kendi module'ümüz:

import calculations # type: ignore

calculations.add(5, 3)


# __name__:

if __name__ == "__main__":

    print("Running directly")


# VEX:

from vex import *


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# import
#     Bir module'ü programa dahil eder.
#
# from ... import
#     Module içerisinden belirli öğeleri alır.
#
# as
#     Module'e farklı/kısa bir isim verir.
#
# __name__
#     Dosyanın nasıl çalıştırıldığını kontrol etmemizi sağlar.
#
# module
#     Bir .py dosyasıdır.
#
# library
#     Bir veya daha fazla module'den oluşabilir.
#
# Büyük VEX projelerinde module kullanmak:
#
#     Kod tekrarını azaltır.
#     Dosyaları küçültür.
#     Takım içerisinde çalışmayı kolaylaştırır.
#     Debug işlemini kolaylaştırır.
#     Robot kodunu daha düzenli hale getirir.






# ============================================================
# Ders 08 bitti, bir sonraki dersten devam edebilirsiniz.
# END OF 08 - MODULES
# ============================================================

