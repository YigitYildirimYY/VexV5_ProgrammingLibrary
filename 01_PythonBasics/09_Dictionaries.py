# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 09 - DICTIONARIES
# ============================================================

# Dictionary, verileri KEY : VALUE şeklinde saklayan
# bir Python veri yapısıdır.
#
# Listede verilere index ile ulaşırız:
#
# numbers[0]
#
# Dictionary'de ise bir KEY kullanırız:
#
# robot["speed"]
#
# VEX programlamada dictionary özellikle robot ayarları,
# configuration değerleri ve isimlendirilmiş veriler için
# kullanışlıdır.


# ============================================================
# 01 - DICTIONARY OLUŞTURMA
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50,
    "mode": "autonomous"
}

print(robot)

# Dictionary {} ile oluşturulur.
#
# Her veri:
#
# "key": value
#
# şeklindedir.


# ============================================================
# 02 - KEY İLE DEĞERE ULAŞMA
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

print(robot["speed"])
print(robot["turn_speed"])

# Dictionary'de index yerine KEY kullanılır.


# ============================================================
# 03 - DEĞER DEĞİŞTİRME
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

robot["speed"] = 100

print(robot)

# Var olan bir KEY'e yeni değer verirsek
# o KEY'in değeri değiştirilir.


# ============================================================
# 04 - YENİ DEĞER EKLEME
# ============================================================

robot = {
    "speed": 80
}

robot["turn_speed"] = 50

print(robot)

# Dictionary'de olmayan bir KEY'e değer verirsek
# yeni eleman oluşturulur.


# ============================================================
# 05 - DEL
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50,
    "mode": "autonomous"
}

del robot["mode"]

print(robot)

# del belirli bir KEY'i ve değerini siler.


# ============================================================
# 06 - POP
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

speed = robot.pop("speed")

print(speed)
print(robot)

# pop() elemanı siler ve silinen değeri return eder.


# ============================================================
# 07 - IN
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

print("speed" in robot)
print("battery" in robot)

# in KEY'in dictionary içerisinde bulunup
# bulunmadığını kontrol eder.


# ============================================================
# 08 - NOT IN
# ============================================================

robot = {
    "speed": 80
}

if "battery" not in robot:

    print("Battery information is missing")


# ============================================================
# 09 - GET
# ============================================================

robot = {
    "speed": 80
}

print(robot.get("speed"))

# get() KEY'in değerini getirir.


# ============================================================
# 10 - GET İLE VAR OLMAYAN KEY
# ============================================================

robot = {
    "speed": 80
}

print(robot.get("battery"))

# KEY yoksa get() hata vermek yerine None döndürür.


# ============================================================
# 11 - GET DEFAULT VALUE
# ============================================================

robot = {
    "speed": 80
}

battery = robot.get("battery", 0)

print(battery)

# KEY bulunamazsa ikinci değer kullanılır.
#
# Burada battery yok.
# Bu nedenle:
#
# battery = 0


# ============================================================
# 12 - KEYS
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50,
    "mode": "autonomous"
}

print(robot.keys())

# keys() bütün KEY'leri verir.


# ============================================================
# 13 - VALUES
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50,
    "mode": "autonomous"
}

print(robot.values())

# values() bütün değerleri verir.


# ============================================================
# 14 - ITEMS
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

print(robot.items())

# items() KEY ve VALUE çiftlerini verir.


# ============================================================
# 15 - DICTIONARY ÜZERİNDE LOOP
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50,
    "max_speed": 100
}

for key in robot:

    print(key)

# Normal loop dictionary'nin KEY'lerini gezer.


# ============================================================
# 16 - KEY VE VALUE BİRLİKTE
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

for key, value in robot.items():

    print(key, value)

# items() sayesinde KEY ve VALUE aynı anda alınabilir.


# ============================================================
# 17 - SADECE VALUE'LAR
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

for value in robot.values():

    print(value)


# ============================================================
# 18 - SADECE KEY'LER
# ============================================================

robot = {
    "speed": 80,
    "turn_speed": 50
}

for key in robot.keys():

    print(key)


# ============================================================
# 19 - FARKLI VERİ TÜRLERİ
# ============================================================

robot = {
    "name": "VEX Robot",
    "speed": 80,
    "enabled": True
}

print(robot)

# Dictionary değerleri farklı veri türlerinde olabilir.


# ============================================================
# 20 - LISTE İÇEREN DICTIONARY
# ============================================================

robot = {
    "speeds": [50, 60, 70],
    "motors": [1, 2, 3, 4, 5, 6]
}

print(robot["speeds"])
print(robot["motors"])

# Dictionary'nin VALUE kısmı list olabilir.


# ============================================================
# 21 - DICTIONARY İÇEREN DICTIONARY
# ============================================================

robot = {
    "drive": {
        "left": 50,
        "right": 60
    }
}

print(robot["drive"]["left"])

# Dictionary'ler iç içe kullanılabilir.


# ============================================================
# 22 - DICTIONARY + FUNCTION
# ============================================================

def show_speed(robot):

    print(robot["speed"])


settings = {
    "speed": 80
}

show_speed(settings)

# Dictionary function'a parameter olarak gönderilebilir.


# ============================================================
# 23 - DICTIONARY İLE AYAR TUTMA
# ============================================================

settings = {
    "max_speed": 100,
    "turn_speed": 60,
    "deadband": 5
}

print(settings["max_speed"])

# Robotun ayarlarını tek bir yapı içerisinde
# toplamak için kullanılabilir.


# ============================================================
# 24 - VEX CONFIGURATION MANTIĞI
# ============================================================

robot_config = {
    "max_speed": 100,
    "drive_speed": 80,
    "turn_speed": 50,
    "deadband": 5
}

speed = robot_config["drive_speed"]

print(speed)

# Bu yapı ileride robotun ayarlarını tek bir yerde
# değiştirmemizi sağlayabilir.
#
# Örneğin robotun hızını değiştirmek için programın
# birçok yerini değiştirmek yerine sadece:
#
# "drive_speed": 80
#
# değerini değiştirebiliriz.


# ============================================================
# 25 - DICTIONARY + CONDITION
# ============================================================

robot = {
    "speed": 80,
    "enabled": True
}

if robot["enabled"]:

    print("Robot enabled")

# Dictionary'deki değerler condition içerisinde
# normal variable gibi kullanılabilir.


# ============================================================
# 26 - DICTIONARY İLE DURUM SAKLAMA
# ============================================================

robot_state = {
    "speed": 50,
    "mode": "manual",
    "enabled": True
}

if robot_state["mode"] == "manual":

    print("Manual mode")


# ============================================================
# 27 - DICTIONARY'Yİ GÜNCELLEME
# ============================================================

robot_state = {
    "speed": 50,
    "mode": "manual"
}

robot_state["speed"] = 80
robot_state["mode"] = "autonomous"

print(robot_state)

# Dictionary değiştirilebilir.
#
# Buna mutable yapı denir.


# ============================================================
# 28 - CLEAR
# ============================================================

robot = {
    "speed": 80,
    "mode": "manual"
}

robot.clear()

print(robot)

# clear() dictionary'nin bütün elemanlarını siler.


# ============================================================
# 29 - DICTIONARY VE LIST FARKI
# ============================================================

numbers = [10, 20, 30]

robot = {
    "speed": 80,
    "turn_speed": 50
}

print(numbers[0])

print(robot["speed"])

# LIST:
#     Index ile erişilir.
#
# DICTIONARY:
#     KEY ile erişilir.
#
# Listeler sıralı veri kümeleri için,
# dictionary'ler isimlendirilmiş veriler için
# daha uygundur.


# ============================================================
# 30 - VEX'TE DICTIONARY KULLANIMI
# ============================================================

robot_config = {
    "drive_speed": 80,
    "turn_speed": 50,
    "max_speed": 100,
    "deadband": 5
}

def get_drive_speed():

    return robot_config["drive_speed"]


print(get_drive_speed())

# Bu yapı gerçek robot projelerinde configuration
# sisteminin temelini oluşturabilir.
#
# Örneğin ileride:
#
# PID ayarları
# motor hızları
# sensör eşikleri
# autonomous ayarları
#
# gibi değerler dictionary içerisinde tutulabilir.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Dictionary:
#     KEY : VALUE yapısında veri tutar.
#
# {}:
#     Dictionary oluşturur.
#
# robot["speed"]:
#     KEY üzerinden değer alır.
#
# robot["speed"] = 100:
#     Değeri değiştirir.
#
# robot["new"] = value:
#     Yeni eleman ekler.
#
# del:
#     Eleman siler.
#
# pop():
#     Elemanı siler ve değerini döndürür.
#
# get():
#     KEY'in değerini güvenli şekilde alır.
#
# keys():
#     KEY'leri verir.
#
# values():
#     VALUE'ları verir.
#
# items():
#     KEY + VALUE çiftlerini verir.
#
# VEX'te dictionary özellikle:
#
#     Robot configuration
#     PID constants
#     Sensor thresholds
#     Autonomous settings
#     Robot state
#
# gibi isimlendirilmiş verileri yönetmek için
# oldukça kullanışlıdır.





# ============================================================
# Ders 09 bitti, bir sonraki dersten devam edebilirsiniz.
# END OF 09 - DICTIONARIES
# ============================================================