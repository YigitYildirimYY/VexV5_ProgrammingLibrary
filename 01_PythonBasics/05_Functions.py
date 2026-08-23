# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 05 - FUNCTIONS
# ============================================================

# Function, belirli bir görevi yapan ve ihtiyaç olduğunda
# tekrar çağrılabilen bir kod bloğudur.
#
# Function kullanmak:
# - kod tekrarını azaltır
# - programı düzenler
# - kodun okunmasını kolaylaştırır
# - büyük robot programlarını parçalara ayırır
#
# Python'da function oluşturmak için "def" kullanılır.


# ============================================================
# 01 - TEMEL FUNCTION
# ============================================================

def hello():
    print("Hello")


hello()

# def hello():
#     Function'ın tanımıdır.
#
# hello()
#     Function'ın çağrılmasıdır.
#
# Tanımlamak function'ı çalıştırmaz.
# Function'ı çalıştırmak için çağırmamız gerekir.


# ============================================================
# 02 - FUNCTION SIRASI
# ============================================================

def first():
    print("First")


def second():
    print("Second")


first()
second()

# Functionlar kullanılmadan önce tanımlanmalıdır.
#
# Bu nedenle büyük projelerde function tanımlarını
# programın uygun bir bölümünde toplamak iyi bir alışkanlıktır.


# ============================================================
# 03 - PARAMETER
# ============================================================

def greet(name):
    print("Hello", name)


greet("Yigit")
greet("Robot")

# name -> parameter
#
# "Yigit" ve "Robot" -> argument
#
# Parameter, function'a dışarıdan veri göndermemizi sağlar.


# ============================================================
# 04 - BİRDEN FAZLA PARAMETER
# ============================================================

def add_numbers(a, b):
    print(a + b)


add_numbers(5, 3)
add_numbers(10, 20)

# Parameterlar virgülle ayrılır.
#
# a ve b function'ın içerisinde kullanılabilir.


# ============================================================
# 05 - RETURN
# ============================================================

def add(a, b):
    return a + b


result = add(5, 3)

print(result)

# return, hesaplanan değeri function'ın dışına gönderir.
#
# Böylece function'ın sonucunu başka bir variable'a
# kaydedebiliriz.


# ============================================================
# 06 - RETURN İLE HESAPLAMA
# ============================================================

def multiply(a, b):
    return a * b


result = multiply(4, 5)

print(result)


# ============================================================
# 07 - RETURN VE PRINT FARKI
# ============================================================

def print_number():
    print(10)


def return_number():
    return 10


print_number()

number = return_number()

print(number)

# print():
#     Değeri ekrana gösterir.
#
# return:
#     Değeri function'ın dışına gönderir.
#
# Program içerisinde sonucu başka yerde kullanacaksak
# return kullanmak gerekir.


# ============================================================
# 08 - RETURN FUNCTION'I BİTİRİR
# ============================================================

def check_number(number):

    if number > 0:
        return "Positive"

    return "Zero or Negative"


print(check_number(10))
print(check_number(-5))

# return çalıştığında function sona erer.
#
# return'den sonra aynı function içerisindeki kod
# çalışmaya devam etmez.


# ============================================================
# 09 - BOOLEAN RETURN
# ============================================================

def is_positive(number):

    return number > 0


print(is_positive(10))
print(is_positive(-10))

# Function doğrudan True veya False döndürebilir.
#
# Bu yapı robot programlarında sensör ve durum
# kontrollerinde çok kullanılacaktır.


# ============================================================
# 10 - FUNCTION + IF
# ============================================================

def check_speed(speed):

    if speed > 100:
        return "Too Fast"

    elif speed < 0:
        return "Reverse"

    else:
        return "Normal"


print(check_speed(120))
print(check_speed(50))
print(check_speed(-20))


# ============================================================
# 11 - DEFAULT PARAMETER
# ============================================================

def show_speed(speed=50):

    print(speed)


show_speed()
show_speed(80)

# speed=50 varsayılan değerdir.
#
# Argument verilmezse:
#     speed = 50
#
# Argument verilirse:
#     verilen değer kullanılır.


# ============================================================
# 12 - DEFAULT PARAMETER İLE HESAPLAMA
# ============================================================

def calculate_power(speed, multiplier=2):

    return speed * multiplier


print(calculate_power(20))
print(calculate_power(20, 3))

# İlk kullanımda multiplier = 2
# İkinci kullanımda multiplier = 3


# ============================================================
# 13 - KEYWORD ARGUMENT
# ============================================================

def subtract(a, b):

    return a - b


result = subtract(a=10, b=3)

print(result)

# Parameter isimlerini çağırırken açıkça yazabiliriz.
#
# Bu özellikle çok fazla parameter olduğunda
# kodun okunmasını kolaylaştırır.


# ============================================================
# 14 - POSITIONAL ARGUMENT
# ============================================================

def divide(a, b):

    return a / b


result = divide(10, 2)

print(result)

# Burada:
#
# 10 -> a
# 2  -> b
#
# Argumentlar sıralarına göre parameterlara atanır.


# ============================================================
# 15 - BİRDEN FAZLA DEĞER RETURN
# ============================================================
"""
def calculate(a, b):

    total = a + b
    difference = a - b

    return total, difference


total, difference = calculate(10, 4)

print(total)
print(difference)
"""
# Python bir function'dan birden fazla değeri
# birlikte döndürebilir.


# ============================================================
# 16 - FUNCTION İÇİNDE FOR
# ============================================================

def count_to_five():

    for number in range(1, 6):
        print(number)


count_to_five()

# Function içerisinde normal Python yapıları
# kullanılabilir.


# ============================================================
# 17 - FUNCTION + LOOP + PARAMETER
# ============================================================

def count_to(limit):

    for number in range(1, limit + 1):
        print(number)


count_to(5)
count_to(10)

# Aynı function farklı limitlerle kullanılabilir.


# ============================================================
# 18 - FUNCTION + WHILE
# ============================================================

def countdown(number):

    while number > 0:

        print(number)

        number -= 1


countdown(5)

# Function ile loop birlikte kullanılabilir.


# ============================================================
# 19 - LOCAL VARIABLE
# ============================================================
"""
def calculate():

    value = 10

    print(value)


calculate()

# value yalnızca function'ın içerisinde oluşturulmuştur.
#
# Buna local variable denir.
"""

# ============================================================
# 20 - GLOBAL VARIABLE
# ============================================================

robot_speed = 50


def show_robot_speed():

    print(robot_speed)


show_robot_speed()

# Function dışında oluşturulan variable,
# function içerisinden okunabilir.
#
# Ancak büyük projelerde global variable kullanımını
# gereksiz yere artırmamak daha sağlıklıdır.


# ============================================================
# 21 - LOCAL VE GLOBAL AYRIMI
# ============================================================

value = 100


def example():

    value = 50

    print(value)


example()

print(value)

# Function içerisindeki value:
#     50
#
# Dışarıdaki value:
#     100
#
# Aynı isimde olsalar bile farklı scope'larda bulunurlar.


# ============================================================
# 22 - FUNCTION'IN FUNCTION ÇAĞIRMASI
# ============================================================

def double(number):

    return number * 2


def calculate(number):

    result = double(number)

    return result + 10


print(calculate(5))

# Bir function başka bir function'ı çağırabilir.
#
# Bu özellik büyük programları parçalara ayırmak
# için çok önemlidir.


# ============================================================
# 23 - FUNCTION + BOOLEAN
# ============================================================
"""
def target_reached(current, target):

    if current >= target:
        return True

    return False


current = 100
target = 100

if target_reached(current, target):
    print("Target reached")
"""

# Function'ın sonucunu if içerisinde doğrudan kullanabiliriz.


# ============================================================
# 24 - DAHA KISA BOOLEAN FUNCTION
# ============================================================

def target_reached(current, target):

    return current >= target


print(target_reached(100, 100))
print(target_reached(50, 100))

# Karşılaştırma zaten True veya False döndürdüğü için
# ekstra if kullanmaya gerek yoktur.


# ============================================================
# 25 - PARAMETER KONTROLÜ
# ============================================================

def limit_speed(speed):

    if speed > 100:
        return 100

    if speed < -100:
        return -100

    return speed


print(limit_speed(150))
print(limit_speed(-150))
print(limit_speed(80))

# Bu yapı ileride motor hızlarını sınırlandırmak için
# gerçek VEX functionlarında kullanılabilir.


# ============================================================
# 26 - VEX FUNCTION'A GEÇİŞ
# ============================================================
"""
# Artık gerçek VEX functionlarının mantığını
# Python açısından biliyoruz.
#
# Örneğin bir motor function'ı teorik olarak:

def drive_forward(speed):
    pass


# pass burada "henüz işlem yapma" anlamına gelir.
#
# Function'ın yapısını göstermek için kullanılır.
#
# Gerçek motor kodunu yazabilmek için önce VEX Motor
# nesnesini ve motor komutlarını öğrenmemiz gerekir.
#
# Bu nedenle burada motoru uydurma şekilde tanımlamıyoruz.
"""

# ============================================================
# 27 - VEX FUNCTION PARAMETER MANTIĞI
# ============================================================

def drive_forward(speed):
    pass


# Örneğin daha sonra:
#
# drive_forward(50)
# drive_forward(80)
#
# şeklinde kullanılabilir.
#
# Burada speed parameter'dır.
#
# Function'ın içerisinde gerçek motor komutlarını
# Motor Library bölümünde yazacağız.


# ============================================================
# 29 - FUNCTION İSİMLERİ
# ============================================================

def calculate_error(target, current):
    return target - current


def check_target(current, target):
    return current >= target







# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# def
#     Function oluşturur.
#
# parameter
#     Function'ın alabileceği değişkendir.
#
# argument
#     Function çağrılırken gönderilen gerçek değerdir.
#
# return
#     Function'dan değer döndürür.
#
# pass
#     Henüz kod yazılmamış function gövdesinde
#     geçici olarak kullanılabilir.
#
# local variable
#     Function içerisinde oluşturulan variable'dır.
#
# global variable
#     Function dışında oluşturulan variable'dır.
#
# Functionların temel amacı:
#
#     Kodu tekrar kullanmak
#     Kodu bölmek
#     Kodu okunabilir yapmak
#     Büyük sistemleri yönetilebilir hale getirmek
#
# VEX'te ileride:
#
#     drive()
#     turn()
#     intake()
#     calculate_error()
#     get_distance()
#
# gibi functionlar oluşturacağız.
#
# Ancak bunları ilgili VEX cihazlarını öğrendikten sonra
# gerçek motor ve sensör kodlarıyla yazacağız.



# ============================================================
# Ders 05 bitti, sıradaki derse geçebilirsiniz.
# END OF 05 - FUNCTIONS
# ============================================================