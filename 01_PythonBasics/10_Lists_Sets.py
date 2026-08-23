# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 10 - TUPLES & SETS
# ============================================================

# Tuple ve Set, Python'daki iki farklı veri yapısıdır.
#
# LIST:
#     [10, 20, 30]
#
# TUPLE:
#     (10, 20, 30)
#
# SET:
#     {10, 20, 30}
#
# Üçü birbirine benzese de kullanım amaçları farklıdır.


# ============================================================
# 01 - TUPLE OLUŞTURMA
# ============================================================

position = (100, 200)

print(position)

# Tuple genellikle () ile oluşturulur.
#
# Tuple içerisindeki değerler sıralıdır.


# ============================================================
# 02 - TUPLE INDEX
# ============================================================

position = (100, 200, 300)

print(position[0])
print(position[1])
print(position[2])

# Tuple'da da index 0'dan başlar.
#
# List ile bu açıdan aynıdır.


# ============================================================
# 03 - TUPLE DEĞİŞTİRİLEMEZ
# ============================================================

position = (100, 200)

# Aşağıdaki kod hatalıdır:
#
# position[0] = 300
#
# Çünkü tuple oluşturulduktan sonra elemanları
# değiştirilemez.
#
# Buna immutable denir.


# ============================================================
# 04 - TUPLE İÇİN LEN
# ============================================================

position = (100, 200, 300)

print(len(position))

# len() tuple'ın eleman sayısını verir.


# ============================================================
# 05 - TUPLE İÇİN FOR
# ============================================================

position = (100, 200, 300)

for value in position:

    print(value)

# Tuple üzerinde loop kullanılabilir.


# ============================================================
# 06 - TUPLE SLICING
# ============================================================

values = (10, 20, 30, 40, 50)

print(values[1:4])

# Tuple slicing, list slicing ile aynı mantıktadır.


# ============================================================
# 07 - TUPLE UNPACKING
# ============================================================

position = (100, 200)

x, y = position

print(x)
print(y)

# Tuple içerisindeki değerleri ayrı variable'lara
# dağıtabiliriz.
#
# Bu işleme unpacking denir.


# ============================================================
# 08 - DAHA FAZLA UNPACKING
# ============================================================

robot_position = (100, 200, 90)

x, y, heading = robot_position

print(x)
print(y)
print(heading)

# Robot programlarında koordinat gibi sabit grupları
# temsil etmek için kullanışlı olabilir.


# ============================================================
# 09 - FUNCTION'DAN TUPLE DÖNDÜRME
# ============================================================

def get_position():

    return 100, 200


x, y = get_position()

print(x)
print(y)

# Python birden fazla değeri tuple olarak döndürebilir.
#
# Bu, Functions konusunda gördüğümüz:
#
# return a, b
#
# yapısının arkasındaki mantıktır.


# ============================================================
# 10 - TUPLE İÇİNDE FARKLI VERİ TÜRLERİ
# ============================================================

robot = ("VEX", 80, True)

print(robot)

# Tuple farklı veri türlerini içerebilir.


# ============================================================
# 11 - TUPLE VE LIST FARKI
# ============================================================

numbers_list = [10, 20, 30]

numbers_tuple = (10, 20, 30)

print(numbers_list)
print(numbers_tuple)

# LIST:
#     Değiştirilebilir.
#
# TUPLE:
#     Değiştirilemez.
#
# Bu nedenle tuple daha çok sabit kalması gereken
# veri gruplarında kullanılır.


# ============================================================
# 12 - TUPLE NE ZAMAN KULLANILIR?
# ============================================================

motor_ports = (1, 2, 3, 4, 5, 6)

print(motor_ports)

# Örneğin motor portlarının sabit bir grup olduğunu
# düşünüyorsak tuple kullanılabilir.
#
# Program çalışırken bu değerlerin yanlışlıkla
# değiştirilmesini istemiyorsak tuple avantajlıdır.


# ============================================================
# 13 - SET OLUŞTURMA
# ============================================================

numbers = {10, 20, 30}

print(numbers)

# Set {} ile oluşturulur.
#
# Ancak dictionary ile karıştırılmamalıdır.
#
# Dictionary:
#
# {"speed": 80}
#
# Set:
#
# {10, 20, 30}


# ============================================================
# 14 - SET SIRALI DEĞİLDİR
# ============================================================

numbers = {30, 10, 20}

print(numbers)

# Set'lerde elemanların belirli bir index sırası
# üzerinden kullanılacağı varsayılmamalıdır.
#
# Bu nedenle:
#
# numbers[0]
#
# kullanılamaz.


# ============================================================
# 15 - SET'TE TEKRARLANAN DEĞERLER
# ============================================================

numbers = {10, 20, 20, 30, 30}

print(numbers)

# Set aynı değeri birden fazla kez tutmaz.
#
# Sonuçta her değer yalnızca bir kez bulunur.


# ============================================================
# 16 - ADD
# ============================================================

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# add() sete yeni eleman ekler.


# ============================================================
# 17 - DUPLICATE ADD
# ============================================================

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)

# 20 zaten bulunduğu için ikinci bir 20 oluşmaz.


# ============================================================
# 18 - REMOVE
# ============================================================

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

# remove() belirtilen elemanı siler.


# ============================================================
# 19 - DISCARD
# ============================================================

numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)

# discard() eleman yoksa hata oluşturmaz.
#
# Bu nedenle elemanın bulunup bulunmadığından emin
# olmadığımız durumlarda kullanışlıdır.


# ============================================================
# 20 - SET İÇİNDE IN
# ============================================================

ports = {1, 2, 3, 4, 5, 6}

print(3 in ports)
print(8 in ports)

# Set'in önemli kullanım alanlarından biri
# hızlı üyelik kontrolüdür.


# ============================================================
# 21 - SET LOOP
# ============================================================

numbers = {10, 20, 30}

for number in numbers:

    print(number)

# Set üzerinde loop kullanılabilir.
#
# Ancak elemanların belirli bir sırada geleceğine
# güvenmemeliyiz.


# ============================================================
# 22 - SET BİRLEŞTİRME
# ============================================================

left_ports = {1, 2, 3}

right_ports = {4, 5, 6}

all_ports = left_ports | right_ports

print(all_ports)

# | iki setin birleşimini oluşturur.


# ============================================================
# 23 - SET INTERSECTION
# ============================================================

first = {1, 2, 3, 4}

second = {3, 4, 5, 6}

common = first & second

print(common)

# & iki sette ortak bulunan elemanları verir.


# ============================================================
# 24 - SET DIFFERENCE
# ============================================================

first = {1, 2, 3, 4}

second = {3, 4, 5, 6}

difference = first - second

print(difference)

# first - second:
#
# first içerisinde olup second içerisinde olmayan
# elemanları verir.


# ============================================================
# 25 - SET SYMMETRIC DIFFERENCE
# ============================================================

first = {1, 2, 3}

second = {3, 4, 5}

result = first ^ second

print(result)

# İki sette ortak olmayan elemanları verir.


# ============================================================
# 26 - SET VE LIST ARASINDA DÖNÜŞÜM
# ============================================================

numbers = [10, 20, 20, 30, 30]

unique_numbers = set(numbers)

print(unique_numbers)

# List'i set'e çevirerek tekrar eden değerleri
# kaldırabiliriz.


# ============================================================
# 27 - SET'TEN LIST'E
# ============================================================

numbers = {10, 20, 30}

number_list = list(numbers)

print(number_list)

# set() ve list() ile veri yapıları arasında
# dönüşüm yapılabilir.
#
# Ancak set sıralı olmadığı için dönüşümden sonra
# belirli bir sıra beklememek gerekir.


# ============================================================
# 28 - VEX'TE TUPLE
# ============================================================

# Örneğin sabit bir koordinatı tuple ile tutabiliriz:

starting_position = (0, 0, 0)

x, y, heading = starting_position

print(x)
print(y)
print(heading)

# Koordinat gibi birlikte anlam ifade eden ve
# değiştirilmemesi gereken veriler için uygundur.


# ============================================================
# 29 - VEX'TE SET
# ============================================================

motor_ports = {1, 2, 3, 4, 5, 6}

if 3 in motor_ports:

    print("Port 3 is used")

# Örneğin hangi portların kullanıldığını kontrol etmek
# için set mantığı kullanılabilir.
#
# Gerçek robot konfigürasyonunda bunun daha gelişmiş
# kullanımını ileride göreceğiz.


# ============================================================
# 30 - KISA REFERANS
# ============================================================

# TUPLE:

position = (100, 200)

print(position[0])


# Tuple unpacking:

x, y = position


# Tuple uzunluğu:

len(position)


# SET:

ports = {1, 2, 3}


# Eleman ekleme:

ports.add(4)


# Eleman silme:

ports.remove(4)


# Güvenli silme:

ports.discard(5)


# Üyelik:

print(3 in ports)


# Birleşim:

a = {1, 2}
b = {2, 3}

print(a | b)


# Kesişim:

print(a & b)


# Fark:

print(a - b)


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# LIST:
#
# [10, 20, 30]
#
# Değiştirilebilir ve sıralıdır.


# TUPLE:
#
# (10, 20, 30)
#
# Değiştirilemez ve sıralıdır.


# SET:
#
# {10, 20, 30}
#
# Tekrarlanan değerleri tutmaz ve index kullanılmaz.


# Tuple:
#     Sabit veri grupları için.


# Set:
#     Benzersiz değerler ve üyelik kontrolü için.


# VEX'te:
#
# List
#     Değişken uzunluktaki veri grupları.
#
# Tuple
#     Sabit koordinatlar, port grupları ve benzeri
#     değişmemesi gereken veri grupları.
#
# Set
#     Benzersiz değerler ve hızlı üyelik kontrolü.
#
# Dictionary
#     İsimlendirilmiş KEY : VALUE verileri.
#
# Bu dört veri yapısını birbirinden ayırmak,
# büyük VEX projelerinde doğru veri yapısını seçmek
# açısından önemlidir.






# ============================================================
# Ders 10 bitti, sıradaki dersle devam edebilirsiniz.
# END OF 10 - TUPLES & SETS
# ============================================================