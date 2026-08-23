# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 06 - LISTS
# ============================================================

# List, birden fazla değeri tek bir variable içerisinde
# saklamamızı sağlayan Python veri yapısıdır.
#
# VEX programlamada listeler özellikle:
# - birden fazla motor/sensör değerini tutmak
# - ölçümleri saklamak
# - birden fazla değeri sırayla işlemek
# - loop ile çok sayıda veriyi kontrol etmek
# için kullanışlıdır.


# ============================================================
# 01 - LIST OLUŞTURMA
# ============================================================

numbers = [10, 20, 30, 40]

print(numbers)

# Listeler [] ile oluşturulur.
#
# Listedeki elemanlar virgülle ayrılır.


# ============================================================
# 02 - FARKLI VERİ TÜRLERİ
# ============================================================

names = ["Left", "Right", "Center"]

speeds = [50, 75, 100]

values = [10, 20.5, 30, 40]

print(names)
print(speeds)
print(values)


# ============================================================
# 03 - INDEX
# ============================================================

numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[1])
print(numbers[2])

# Python'da index 0'dan başlar.
#
# numbers:
#
# 10 -> index 0
# 20 -> index 1
# 30 -> index 2
# 40 -> index 3


# ============================================================
# 04 - NEGATIVE INDEX
# ============================================================

numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])

# -1 -> son eleman
# -2 -> sondan ikinci eleman


# ============================================================
# 05 - LIST ELEMANINI DEĞİŞTİRME
# ============================================================

numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)

# Sonuç:
#
# [10, 50, 30]
#
# Belirli bir index'e yeni değer atayabiliriz.


# ============================================================
# 06 - APPEND
# ============================================================

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# append() listenin sonuna yeni bir eleman ekler.


# ============================================================
# 07 - BİRDEN FAZLA APPEND
# ============================================================

numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)

print(numbers)

# Boş bir liste oluşturup elemanları sonradan
# ekleyebiliriz.


# ============================================================
# 08 - INSERT
# ============================================================

numbers = [10, 30, 40]

numbers.insert(1, 20)

print(numbers)

# insert(index, value)
#
# 1. parameter -> nereye?
# 2. parameter -> ne ekleniyor?


# ============================================================
# 09 - REMOVE
# ============================================================

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

# remove() verilen değerin ilk karşılaştığı elemanı siler.
#
# Burada ilk 20 silinir.


# ============================================================
# 10 - POP
# ============================================================

numbers = [10, 20, 30]

value = numbers.pop()

print(value)
print(numbers)

# pop() son elemanı listeden çıkarır
# ve çıkardığı değeri return eder.


# ============================================================
# 11 - INDEX İLE POP
# ============================================================

numbers = [10, 20, 30, 40]

value = numbers.pop(1)

print(value)
print(numbers)

# pop(1):
# index 1'deki elemanı çıkarır.


# ============================================================
# 12 - LEN
# ============================================================

numbers = [10, 20, 30, 40]

print(len(numbers))

# len() listedeki eleman sayısını verir.


# ============================================================
# 13 - LISTE ÜZERİNDE FOR
# ============================================================

numbers = [10, 20, 30, 40]

for number in numbers:

    print(number)

# Bu yapı listedeki bütün elemanları sırayla gezer.


# ============================================================
# 14 - INDEX İLE FOR
# ============================================================

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):

    print(i, numbers[i])

# i -> index
# numbers[i] -> o index'teki değer


# ============================================================
# 15 - LISTE İÇİNDE IF
# ============================================================

numbers = [10, 50, 120, 30]

for number in numbers:

    if number > 50:

        print(number)

# Listedeki her eleman kontrol edilir.


# ============================================================
# 16 - LISTEYE HESAPLANMIŞ DEĞERLER EKLEME
# ============================================================

numbers = []

for number in range(1, 6):

    numbers.append(number * 10)


print(numbers)

# Sonuç:
#
# [10, 20, 30, 40, 50]


# ============================================================
# 17 - LISTEDEN TOPLAM ALMA
# ============================================================

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:

    total += number


print(total)

# Bu yöntemle listedeki değerleri tek tek işleyebiliriz.


# ============================================================
# 18 - LISTEDEN ORTALAMA
# ============================================================

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:

    total += number


average = total / len(numbers)

print(average)

# Bu mantık sensör verilerinin ortalamasını almak için
# ileride kullanılabilir.


# ============================================================
# 19 - IN OPERATÖRÜ
# ============================================================

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)

# in:
# Bir değerin listede bulunup bulunmadığını kontrol eder.
#
# Sonuç True veya False olur.


# ============================================================
# 20 - NOT IN
# ============================================================

numbers = [10, 20, 30]

print(50 not in numbers)
print(20 not in numbers)

# not in:
# Değerin listede bulunmadığını kontrol eder.


# ============================================================
# 21 - LISTE KOPYALAMA
# ============================================================

numbers = [10, 20, 30]

copy_numbers = numbers.copy()

copy_numbers.append(40)

print(numbers)
print(copy_numbers)

# copy() bağımsız bir liste oluşturur.
#
# Böylece bir listeyi değiştirirken diğerini
# değiştirmemiş oluruz.


# ============================================================
# 22 - LISTE BİRLEŞTİRME
# ============================================================

left = [10, 20, 30]

right = [40, 50, 60]

all_numbers = left + right

print(all_numbers)

# + iki listeyi birleştirir.


# ============================================================
# 23 - LISTE ÇARPMA
# ============================================================

numbers = [0]

result = numbers * 5

print(result)

# Liste bir sayı ile çarpıldığında elemanlar tekrar edilir.


# ============================================================
# 24 - SLICING
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Sonuç:
#
# [20, 30, 40]
#
# 1 dahil edilir.
# 4 dahil edilmez.


# ============================================================
# 25 - LISTENİN BAŞINDAN VE SONUNDAN SLICING
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

print(numbers[2:])

# [:3]
# İlk üç eleman
#
# [2:]
# Index 2'den sonuna kadar


# ============================================================
# 26 - SORT
# ============================================================

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

# sort() listeyi küçükten büyüğe sıralar.


# ============================================================
# 27 - REVERSE
# ============================================================

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# reverse() listenin sırasını ters çevirir.


# ============================================================
# 28 - NESTED LIST
# ============================================================

robot = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(robot[0])
print(robot[0][1])

# Listelerin içinde başka listeler bulunabilir.
#
# robot[0]    -> [10, 20]
# robot[0][1] -> 20
#
# Büyük veri yapılarında kullanılabilir.


# ============================================================
# 29 - LIST + FUNCTION
# ============================================================

def calculate_average(numbers):

    total = 0

    for number in numbers:

        total += number

    return total / len(numbers)


values = [10, 20, 30, 40]

average = calculate_average(values)

print(average)

# Listeler function parameter olarak gönderilebilir.


# ============================================================
# 30 - VEX'TE LIST MANTIĞI
# ============================================================

# VEX programlarında listeler özellikle sensör verileri,
# motor değerleri veya birden fazla ölçümü saklamak için
# kullanılabilir.
#
# Örneğin:

sensor_values = [20, 25, 23, 24, 22]

total = 0

for value in sensor_values:

    total += value


average = total / len(sensor_values)

print(average)

# Daha sonra gerçek sensörden aldığımız değerleri
# bu listeye ekleyebiliriz:
#
# sensor_values.append(new_value)
#
# Böylece geçmiş ölçümleri saklayabiliriz.
#
# Bu mantık ileride Sensor Data Processing ve
# PID konularında işimize yarayacak.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# List:
#     Birden fazla değeri tek yapıda saklar.
#
# Index:
#     Listedeki elemanın konumudur.
#     İlk index 0'dır.
#
# append():
#     Sona eleman ekler.
#
# insert():
#     Belirli konuma eleman ekler.
#
# remove():
#     Belirli değeri siler.
#
# pop():
#     Elemanı çıkarır ve değeri döndürür.
#
# len():
#     Eleman sayısını verir.
#
# in:
#     Elemanın listede olup olmadığını kontrol eder.
#
# copy():
#     Listenin bağımsız kopyasını oluşturur.
#
# slicing:
#     Listenin belirli bölümünü alır.
#
# Listelerin en önemli avantajı:
#     Aynı türden veya farklı türden birçok veriyi
#     tek bir variable üzerinden yönetebilmemizdir.
#
# VEX'te özellikle sensör verileri, motor grupları ve
# tekrarlanan ölçümler üzerinde çalışırken listeler
# oldukça kullanışlı olacaktır.






# ============================================================
# Ders 06 bitti, sıradaki derse geçebilirsiniz.
# END OF 06 - LISTS
# ============================================================