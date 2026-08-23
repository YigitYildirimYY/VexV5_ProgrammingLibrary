from vex import *

# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 02 - OPERATORS
# ============================================================

# ============================================================
# 1. OPERATORS NEDİR?
# ============================================================
#
# Operator'ler Python'da değerler üzerinde işlem yapmamızı
# sağlayan sembol veya anahtar kelimelerdir.
#
# Örneğin:
#
#     10 + 5
#
# Burada "+" bir operatördür.
#
# Operator'ler özellikle robot programlamada sürekli
# karşımıza çıkar. Ancak şu aşamada amacımız yalnızca
# Python'daki operator'leri öğrenmektir.
#
# Python'daki temel operator grupları:
#
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Assignment Operators
#
# Ayrıca operatorlerin hangi sırayla çalıştığını belirleyen
# "operator precedence" konusu da önemlidir.


# ============================================================
# 2. ARITHMETIC OPERATORS
# ============================================================
#
# Arithmetic operator'ler matematiksel işlemler yapmak için
# kullanılır.
#
# Python'daki temel arithmetic operator'ler:
#
#     +       Toplama
#     -       Çıkarma
#     *       Çarpma
#     /       Bölme
#     //      Tam sayı bölmesi
#     %       Modulo / kalan
#     **      Üs alma
#
# Şimdi bunları tek tek inceleyelim.


# ============================================================
# 3. TOPLAMA +
# ============================================================
#
# "+" iki değeri toplar.

a = 10
b = 5

result = a + b

print(result)

# Çıktı:
#
# 15


# Değişkenleri doğrudan değiştirmek zorunda değiliz.
# Sonucu başka bir değişkende saklayabiliriz.

first_number = 20
second_number = 30

sum_result = first_number + second_number

print(sum_result)

# Çıktı:
#
# 50


# ------------------------------------------------------------
# VEX BAĞLANTISI
# ------------------------------------------------------------
#
# İleride robot hareketlerini kontrol ederken iki değeri
# birleştirmek için toplama kullanacağız.
#
# Örneğin bir temel hız değerine düzeltme eklemek:

base_speed = 50
correction = 10

motor_speed = base_speed + correction

print(motor_speed)

# motor_speed = 60
#
# Burada henüz motor çalıştırmıyoruz.
# Sadece "+" operatorünün robot programlamadaki kullanımını
# görüyoruz.


# ============================================================
# 4. ÇIKARMA -
# ============================================================
#
# "-" iki değer arasındaki farkı bulmak için kullanılır.

a = 20
b = 8

result = a - b

print(result)

# Çıktı:
#
# 12


# Sonuç negatif de olabilir:

a = 8
b = 20

result = a - b

print(result)

# Çıktı:
#
# -12


# Python negatif sayılarla da normal şekilde matematiksel
# işlemler yapabilir.


# ------------------------------------------------------------
# VEX BAĞLANTISI
# ------------------------------------------------------------
#
# Robot programlamada iki değer arasındaki farkı bulmak
# oldukça yaygındır.
#
# Örneğin:

target = 100
current = 80

difference = target - current

print(difference)

# difference = 20
#
# Burada yalnızca çıkarma işlemini kullanıyoruz.
# "error" gibi kontrol sistemi kavramlarını daha ileride
# kendi derslerinde inceleyeceğiz.


# ============================================================
# 5. ÇARPMA *
# ============================================================
#
# "*" çarpma işlemini yapar.

a = 10
b = 5

result = a * b

print(result)

# Çıktı:
#
# 50


# Değişkenlerle:

speed = 50
multiplier = 2

result = speed * multiplier

print(result)

# 100


# Ondalıklı sayılarla da çalışabilir:

speed = 80
factor = 0.5

result = speed * factor

print(result)

# 40.0


# ------------------------------------------------------------
# VEX BAĞLANTISI
# ------------------------------------------------------------
#
# Bir değeri belirli bir oranla değiştirmek gerektiğinde
# çarpma kullanabiliriz.
#
# Örneğin bir değerin %75'ini almak:

value = 100
percentage = 0.75

result = value * percentage

print(result)

# 75.0


# ============================================================
# 6. BÖLME /
# ============================================================
#
# "/" normal bölme işlemini yapar.

a = 20
b = 5

result = a / b

print(result)

# 4.0


# Dikkat:
#
# Python "/" kullandığında sonuç çoğu durumda float olur.
#
# Örneğin:

result = 10 / 2

print(result)

# 5.0
#
# Sonucun matematiksel olarak 5 olmasına rağmen Python bunu
# float olarak saklar.


# Ondalıklı sonuç:

result = 10 / 4

print(result)

# 2.5


# ============================================================
# 7. TAM SAYI BÖLMESİ //
# ============================================================
#
# "//" operatorü floor division olarak adlandırılır.
#
# Bölme işleminin aşağı yuvarlanmış sonucunu verir.

result = 10 // 3

print(result)

# 3


# Normal bölme:

result = 10 / 3

print(result)

# 3.333333...


# Tam sayı bölmesi:

result = 10 // 3

print(result)

# 3


# Negatif sayılarda dikkat edilmesi gereken bir nokta vardır:

result = -10 // 3

print(result)

# Sonuç:
#
# -4
#
# Çünkü Python sonucu aşağı doğru yuvarlar.


# ============================================================
# 8. MODULO %
# ============================================================
#
# "%" operatorü bölme işleminden kalan değeri verir.
#
# Örneğin:
#
# 10 / 3
#
# 3 kere 3 = 9
# kalan = 1

result = 10 % 3

print(result)

# 1


# Başka örnek:

result = 20 % 5

print(result)

# 0
#
# Çünkü 20, 5'e tam bölünür.


# ------------------------------------------------------------
# MODULO'NUN ÖNEMLİ BİR KULLANIMI
# ------------------------------------------------------------
#
# Bir sayının çift olup olmadığını kontrol etmek için
# modulo kullanabiliriz.
#
# Çift sayıların 2'ye bölümünden kalan 0'dır.

number = 10

if number % 2 == 0:
    print("Even")

# 10 % 2 = 0 olduğu için "Even" yazdırılır.
#
# Buradaki "if" kullanımını şu anda detaylı incelemiyoruz.
# Sadece modulo operatorünün bir kullanımını göstermek için
# kullanıyoruz.
#
# Conditions konusu daha sonra ayrı bir dosyada ele alınacak.


# Tek sayı:

number = 7

if number % 2 != 0:
    print("Odd")

# 7 % 2 = 1 olduğu için sayı tektir.


# ============================================================
# 9. ÜS ALMA **
# ============================================================
#
# "**" operatorü üs alma işlemi yapar.

result = 2 ** 3

print(result)

# 8
#
# Çünkü:
#
# 2 × 2 × 2 = 8


# Başka bir örnek:

number = 5

squared = number ** 2

print(squared)

# 25


# Küp:

cubed = number ** 3

print(cubed)

# 125


# Ondalıklı sayılarla da çalışabilir:

result = 4 ** 0.5

print(result)

# 2.0


# ============================================================
# 10. ARITHMETIC OPERATORLERİN ÖZETİ
# ============================================================
#
# +     Toplama
# -     Çıkarma
# *     Çarpma
# /     Bölme
# //    Tam sayı bölmesi
# %     Kalan
# **    Üs alma


# ============================================================
# 11. COMPARISON OPERATORS
# ============================================================
#
# Comparison operator'ler iki değeri karşılaştırır.
#
# Sonuç bir boolean değerdir:
#
#     True
#     False
#
# Temel comparison operator'ler:
#
#     ==      Eşit mi?
#     !=      Eşit değil mi?
#     >       Büyük mü?
#     <       Küçük mü?
#     >=      Büyük veya eşit mi?
#     <=      Küçük veya eşit mi?


# ============================================================
# 12. EŞİTLİK ==
# ============================================================
#
# "==" iki değerin birbirine eşit olup olmadığını kontrol
# eder.
#
# Sonuç True veya False olur.

a = 10
b = 10

result = a == b

print(result)

# True


# Değerler farklıysa:

a = 10
b = 20

result = a == b

print(result)

# False


# ------------------------------------------------------------
# ÇOK ÖNEMLİ
# ------------------------------------------------------------
#
# "=" ile "==" aynı şey değildir.
#
# "=":
# Değişkene değer atar.
#
# "==":
# İki değeri karşılaştırır.
#
# Örneğin:

speed = 50

# Burada speed'e 50 atanıyor.
#
# Karşılaştırma:

print(speed == 50)

# True


# ============================================================
# 13. EŞİT DEĞİL !=
# ============================================================
#
# "!=" iki değerin birbirine eşit olmadığını kontrol eder.

a = 10
b = 20

print(a != b)

# True


a = 10
b = 10

print(a != b)

# False


# ============================================================
# 14. BÜYÜKTÜR >
# ============================================================
#
# ">" sol taraftaki değerin sağ taraftaki değerden büyük
# olup olmadığını kontrol eder.

a = 20
b = 10

print(a > b)

# True


a = 5
b = 10

print(a > b)

# False


# ============================================================
# 15. KÜÇÜKTÜR <
# ============================================================

a = 5
b = 10

print(a < b)

# True


a = 20
b = 10

print(a < b)

# False


# ============================================================
# 16. BÜYÜK VEYA EŞİT >=
# ============================================================
#
# Değerin diğerinden büyük veya ona eşit olup olmadığını
# kontrol eder.

a = 10
b = 10

print(a >= b)

# True
#
# Çünkü eşitler.


a = 20
b = 10

print(a >= b)

# True
#
# Çünkü 20, 10'dan büyüktür.


# ============================================================
# 17. KÜÇÜK VEYA EŞİT <=
# ============================================================

a = 10
b = 10

print(a <= b)

# True


a = 5
b = 10

print(a <= b)

# True


a = 20
b = 10

print(a <= b)

# False


# ============================================================
# 18. COMPARISON OPERATORLERİYLE BOOLEAN
# ============================================================
#
# Comparison operatorlerin sonucu bir boolean'dır.

speed = 80

is_fast = speed > 50

print(is_fast)

# True


# Başka bir örnek:

temperature = 40

is_safe = temperature < 70

print(is_safe)

# True


# Burada:
#
# is_fast
# is_safe
#
# değişkenlerinin kendileri boolean değer taşır.


# ============================================================
# 19. STRING KARŞILAŞTIRMASI
# ============================================================
#
# Comparison operator'ler sadece sayılarla kullanılmaz.
# String'ler de karşılaştırılabilir.

robot_name = "High Skates"

print(robot_name == "High Skates")

# True


print(robot_name == "Other Robot")

# False


# String karşılaştırmalarını ileride daha detaylı
# kullanacağız.


# ============================================================
# 20. LOGICAL OPERATORS
# ============================================================
#
# Logical operator'ler boolean değerleri birleştirmek veya
# değiştirmek için kullanılır.
#
# Üç temel logical operator vardır:
#
#     and
#     or
#     not


# ============================================================
# 21. AND
# ============================================================
#
# "and" kullanıldığında iki koşulun da True olması gerekir.
#
# True and True   -> True
# True and False  -> False
# False and True  -> False
# False and False -> False

a = True
b = True

print(a and b)

# True


a = True
b = False

print(a and b)

# False


# ------------------------------------------------------------
# SAYILARLA KULLANIM
# ------------------------------------------------------------

speed = 80
distance = 100

result = speed > 50 and distance < 200

print(result)

# True
#
# Çünkü:
#
# speed > 50
# -> True
#
# distance < 200
# -> True
#
# True and True
# -> True


# ============================================================
# 22. OR
# ============================================================
#
# "or" koşullardan en az birinin True olması durumunda
# True verir.
#
# True or True   -> True
# True or False  -> True
# False or True  -> True
# False or False  -> False

a = False
b = True

print(a or b)

# True


a = False
b = False

print(a or b)

# False


# ------------------------------------------------------------
# SAYILARLA KULLANIM
# ------------------------------------------------------------

speed = 80
distance = 500

result = speed > 100 or distance < 200

print(result)

# True
#
# Çünkü:
#
# speed > 100
# -> False
#
# distance < 200
# -> False
#
# Bu örnekte iki koşul da False olduğu için sonuç False olur.


# ============================================================
# 23. NOT
# ============================================================
#
# "not" boolean değerin tersini verir.
#
# not True  -> False
# not False -> True

a = True

print(not a)

# False


a = False

print(not a)

# True


# Comparison sonucu üzerinde de kullanılabilir:

speed = 40

result = not (speed > 50)

print(result)

# True
#
# Çünkü:
#
# speed > 50
# -> False
#
# not False
# -> True


# ============================================================
# 24. LOGICAL OPERATORLERİN ÖZETİ
# ============================================================
#
# AND:
#
# İki tarafın da True olması gerekir.
#
# OR:
#
# En az bir taraf True olmalıdır.
#
# NOT:
#
# Boolean değeri tersine çevirir.


# ============================================================
# 25. ASSIGNMENT OPERATORS
# ============================================================
#
# Assignment operator'ler değişkenlere değer atamak veya
# mevcut değerlerini değiştirmek için kullanılır.
#
# En temel assignment operator:
#
#     =
#
# Bunun yanında kısaltılmış matematiksel atamalar vardır:
#
#     +=
#     -=
#     *=
#     /=
#     //=
#     %=
#     **=


# ============================================================
# 26. = OPERATORÜ
# ============================================================
#
# "=" sağ taraftaki değeri sol taraftaki değişkene atar.

speed = 50

print(speed)

# 50


# Daha sonra değeri değiştirebiliriz:

speed = 80

print(speed)

# 80


# ============================================================
# 27. += OPERATORÜ
# ============================================================
#
# Şu işlemi:

number = 10

number = number + 5

print(number)

# şu şekilde kısaltabiliriz:

number = 10

number += 5

print(number)

# Her iki durumda da sonuç:
#
# 15


# ============================================================
# 28. -= OPERATORÜ
# ============================================================

number = 10

number -= 3

print(number)

# 7


# Uzun hali:
#
# number = number - 3


# ============================================================
# 29. *= OPERATORÜ
# ============================================================

number = 10

number *= 3

print(number)

# 30


# Uzun hali:
#
# number = number * 3


# ============================================================
# 30. /= OPERATORÜ
# ============================================================

number = 20

number /= 4

print(number)

# 5.0


# Uzun hali:
#
# number = number / 4


# ============================================================
# 31. //= OPERATORÜ
# ============================================================

number = 20

number //= 3

print(number)

# 6


# Uzun hali:
#
# number = number // 3


# ============================================================
# 32. %= OPERATORÜ
# ============================================================

number = 20

number %= 6

print(number)

# 2
#
# Çünkü:
#
# 20 / 6
# = 3 kalan 2


# ============================================================
# 33. **= OPERATORÜ
# ============================================================

number = 2

number **= 4

print(number)

# 16


# Uzun hali:
#
# number = number ** 4


# ============================================================
# 34. OPERATOR PRECEDENCE
# ============================================================
#
# Bir ifadede birden fazla operator varsa Python bunları
# belirli bir sıraya göre çalıştırır.
#
# Örneğin:

result = 10 + 5 * 2

print(result)

# Sonuç:
#
# 20
#
# Python önce:
#
# 5 * 2
#
# işlemini yapar.
#
# Sonra:
#
# 10 + 10
#
# yapılır.


# ============================================================
# 35. PARANTEZLER
# ============================================================
#
# İşlemin sırasını değiştirmek için parantez kullanabiliriz.

result = (10 + 5) * 2

print(result)

# 30
#
# Önce:
#
# 10 + 5 = 15
#
# Daha sonra:
#
# 15 * 2 = 30


# ============================================================
# 36. OPERATOR PRECEDENCE SIRASI
# ============================================================
#
# Bu aşamada bilmemiz gereken temel sıra:
#
# 1. ()
#
# 2. **
#
# 3. *, /, //, %
#
# 4. +, -
#
# 5. Comparison operators
#
# 6. not
#
# 7. and
#
# 8. or
#
# Örneğin:

result = 10 + 2 * 3

print(result)

# Önce:
#
# 2 * 3 = 6
#
# Sonra:
#
# 10 + 6 = 16


# Parantez kullanırsak:

result = (10 + 2) * 3

print(result)

# Önce:
#
# 10 + 2 = 12
#
# Sonra:
#
# 12 * 3 = 36


# ============================================================
# 37. KARMAŞIK ARITHMETIC İFADELER
# ============================================================
#
# Birden fazla arithmetic operator aynı ifadede bulunabilir.

a = 10
b = 5
c = 2

result = a + b * c

print(result)

# Önce:
#
# 5 * 2 = 10
#
# Daha sonra:
#
# 10 + 10 = 20


# Parantez kullanırsak:

result = (a + b) * c

print(result)

# 30


# ============================================================
# 38. COMPARISON + LOGICAL OPERATORS
# ============================================================
#
# Comparison ve logical operatorler birlikte çok sık
# kullanılır.

speed = 80
distance = 100

condition = speed > 50 and distance < 200

print(condition)

# True


# İfadeyi parçalara ayırabiliriz:

speed_condition = speed > 50
distance_condition = distance < 200

condition = speed_condition and distance_condition

print(condition)

# Bu iki kullanım aynı mantığa sahiptir.


# ============================================================
# 39. OPERATORLERLE VEX ÖRNEĞİ
# ============================================================
#
# Şimdi henüz motor veya sensor kullanmadan,
# operatorlerin robot programlamadaki matematiksel kullanımına
# basit bir örnek verelim.
#
# Bir robotun sol ve sağ tarafına farklı hız vermek
# istediğimizi düşünelim.

forward = 60
turn = 20

left_speed = forward + turn
right_speed = forward - turn

print(left_speed)
print(right_speed)

# Sonuç:
#
# left_speed = 80
# right_speed = 40
#
# Burada sadece:
#
# +
# -
#
# operatorlerini kullandık.


# ============================================================
# 40. NEGATİF DEĞERLER
# ============================================================
#
# Robot programlamada negatif değerler ileride sıkça
# kullanılacaktır.
#
# Python'da negatif sayılar normal şekilde kullanılabilir.

speed = -50

print(speed)

# -50


# Operatorlerle:

speed = -50

speed += 20

print(speed)

# -30


speed -= 10

print(speed)

# -40


# ============================================================
# 41. OPERATORLERDE VERİ TİPLERİ
# ============================================================
#
# Operatorlerin davranışı veri tipine göre değişebilir.
#
# Örneğin sayılarda "+" matematiksel toplama yapar:

a = 10
b = 20

print(a + b)

# 30


# Stringlerde "+" metinleri birleştirir:

first_name = "High"
second_name = "Skates"

print(first_name + " " + second_name)

# High Skates


# ============================================================
# 42. STRING + INTEGER
# ============================================================
#
# String ile integer doğrudan toplanamaz.

speed = 80

# Bu kullanım hatalıdır:
#
# message = "Speed: " + speed
#
# Çünkü:
#
# "Speed: "
#
# bir string,
#
# speed
#
# ise integer'dır.


# Bunun yerine str() ile integer'ı string'e çevirebiliriz:

message = "Speed: " + str(speed)

print(message)

# Speed: 80


# Bu konu ileride print() ve string işlemlerinde daha
# detaylı kullanılacaktır.


# ============================================================
# 43. OPERATORLERİN BİRLİKTE KULLANILMASI
# ============================================================
#
# Bir ifadede birden fazla operator bulunabilir.

a = 10
b = 5
c = 2

result = (a + b) * c - 5

print(result)

# Önce:
#
# a + b
# = 15
#
# Sonra:
#
# 15 * 2
# = 30
#
# Sonra:
#
# 30 - 5
# = 25


# ============================================================
# 44. KÜÇÜK BİR VEX HESAPLAMA ÖRNEĞİ
# ============================================================
#
# Robotumuzun temel hızının 70 olduğunu ve bunun üzerine
# 15 eklemek istediğimizi düşünelim.

base_speed = 70
additional_speed = 15

final_speed = base_speed + additional_speed

print(final_speed)

# 85


# Hızı yarıya indirmek:

final_speed /= 2

print(final_speed)

# 42.5


# Burada:
#
# +
# /=
#
# operatorlerini kullandık.


# ============================================================
# 45. OPERATORLERLE BASİT HESAP MAKİNESİ
# ============================================================
#
# Operatorleri daha iyi anlamak için küçük bir hesaplama
# sistemi oluşturabiliriz.

a = 20
b = 6

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
remainder = a % b

print("Addition:")
print(addition)

print("Subtraction:")
print(subtraction)

print("Multiplication:")
print(multiplication)

print("Division:")
print(division)

print("Remainder:")
print(remainder)


# ============================================================
# 46. OPERATORLERİN VEX PROGRAMLAMADAKİ YERİ
# ============================================================
#
# Şu anda yalnızca operatorleri öğreniyoruz.
# Fakat ileride bunları birçok yerde kullanacağız.
#
# + ve -
# -> değerler arasındaki farklar ve hesaplamalar
#
# *
# -> katsayılarla çarpma ve ölçekleme
#
# /
# -> oran ve bölme işlemleri
#
# %
# -> kalan ve döngüsel hesaplamalar
#
# ==
# !=
# >
# <
# >=
# <=
# -> değerleri karşılaştırma
#
# and
# or
# not
# -> birden fazla boolean ifadeyi birleştirme
#
# =
# +=
# -=
# *=
# /=
# -> değişkenleri güncelleme
#
# Bu operatorlerin tamamı ileride yazacağımız daha büyük
# VEX sistemlerinin temelinde bulunacaktır.




# ============================================================
# 47. ÖZET
# ============================================================
#
# Arithmetic Operators:
#
# +       Toplama
# -       Çıkarma
# *       Çarpma
# /       Bölme
# //      Tam sayı bölmesi
# %       Kalan
# **      Üs alma
#
#
# Comparison Operators:
#
# ==      Eşit
# !=      Eşit değil
# >       Büyük
# <       Küçük
# >=      Büyük veya eşit
# <=      Küçük veya eşit
#
#
# Logical Operators:
#
# and     Ve
# or      Veya
# not     Değil
#
#
# Assignment Operators:
#
# =       Atama
# +=      Topla ve ata
# -=      Çıkar ve ata
# *=      Çarp ve ata
# /=      Böl ve ata
# //=     Tam böl ve ata
# %=      Kalanı ata
# **=     Üs al ve ata
#
#
# Operator precedence:
#
# ()
# **
# *, /, //, %
# +, -
# comparison
# not
# and
# or




# ============================================================
# Ders 02 bitti, bir sonraki dersle devam edebilirsiniz.
# END OF 02 - OPERATORS
# ============================================================