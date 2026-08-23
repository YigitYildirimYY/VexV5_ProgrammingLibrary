# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 11 - EXCEPTIONS
# ============================================================

# Exception, program çalışırken ortaya çıkan beklenmeyen
# bir durumdur.
#
# Örneğin:
#
# int("hello")
#
# Python "hello" değerini sayıya çeviremez ve
# ValueError oluşturur.
#
# Exception handling, bu durumları kontrollü şekilde
# yönetmemizi sağlar.


# ============================================================
# 01 - EXCEPTION NEDİR?
# ============================================================

# Aşağıdaki kod ValueError oluşturur:
#
# number = int("hello")
#
# Program burada normal şekilde devam edemez.
#
# Exception'lar her zaman programlama hatası anlamına
# gelmez. Bazen kullanıcıdan yanlış veri gelmesi gibi
# beklenebilecek durumları yönetmek için kullanılır.


# ============================================================
# 02 - TRY
# ============================================================
"""
try: 

    number = int("100")

    print(number)
"""
# try bloğuna hata çıkma ihtimali olan kod yazılır.
#
# Hata çıkmazsa kod normal şekilde çalışır.


# ============================================================
# 03 - EXCEPT
# ============================================================

try:

    number = int("hello")

except:

    print("Conversion failed")

# try içerisinde exception oluşursa
# except bloğu çalışır.
#
# Böylece programın kontrolünü ele alabiliriz.


# ============================================================
# 04 - BELİRLİ EXCEPTION YAKALAMA
# ============================================================

try:

    number = int("hello")

except ValueError:

    print("Invalid number")

# Sadece beklediğimiz exception'ı yakalamak
# genellikle daha doğru bir yöntemdir.
#
# Burada yalnızca ValueError yakalanır.


# ============================================================
# 05 - VALUEERROR
# ============================================================

try:

    number = int("robot")

except ValueError:

    print("This is not a number")

# ValueError genellikle değer doğru türde görünse bile
# beklenen biçime uygun olmadığında ortaya çıkar.
#
# int("100")  -> çalışır
# int("robot") -> ValueError


# ============================================================
# 06 - TYPEERROR
# ============================================================

try:

    result = "VEX" + 10 # type: ignore

except TypeError:

    print("Wrong data types")

# TypeError, bir işlemin veri türleriyle uyumsuz
# şekilde yapılması durumunda oluşabilir.
#
# String + integer doğrudan yapılamaz.


# ============================================================
# 07 - INDEXERROR
# ============================================================

numbers = [10, 20, 30]

try:

    print(numbers[10])

except IndexError:

    print("Index does not exist")

# Listenin olmayan bir index'ine erişmek
# IndexError oluşturur.


# ============================================================
# 08 - KEYERROR
# ============================================================

robot = {
    "speed": 80
}

try:

    print(robot["battery"])

except KeyError:

    print("Key does not exist")

# Dictionary'de olmayan bir KEY'e [] ile erişmek
# KeyError oluşturur.
#
# Alternatif olarak:
#
# robot.get("battery")
#
# kullanılabilir.


# ============================================================
# 09 - ZERODIVISIONERROR
# ============================================================

try:

    result = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero")

# Bir sayıyı sıfıra bölmeye çalışmak
# ZeroDivisionError oluşturur.


# ============================================================
# 10 - BİRDEN FAZLA EXCEPT
# ============================================================

try:

    number = int("hello")

except ValueError:

    print("Invalid value")

except TypeError:

    print("Wrong data type")

# Farklı exception türleri için farklı işlemler
# tanımlayabiliriz.
#
# Python oluşan hataya uygun except bloğunu çalıştırır.


# ============================================================
# 11 - ELSE
# ============================================================

try:

    number = int("100")

except ValueError:

    print("Invalid number")

else:

    print("Conversion successful")

# else yalnızca try başarılı olursa çalışır.
#
# Yani:
#
# Hata varsa     -> except
# Hata yoksa     -> else


# ============================================================
# 12 - FINALLY
# ============================================================

try:

    number = int("100")

except ValueError:

    print("Invalid number")

finally:

    print("Finished")

# finally her durumda çalışır.
#
# Exception oluşsa da oluşmasa da çalışır.


# ============================================================
# 13 - TRY / EXCEPT / ELSE / FINALLY
# ============================================================

try:

    number = int("100")

except ValueError:

    print("Invalid number")

else:

    print(f"Number: {number}")

finally:

    print("Process finished")

# Genel yapı:
#
# try
#     Ana kod
#
# except
#     Hata olursa
#
# else
#     Hata olmazsa
#
# finally
#     Her durumda


# ============================================================
# 14 - EXCEPTION MESAJINI ALMA
# ============================================================

try:

    number = int("hello")

except ValueError as error:

    print(error)

# "as error" ile exception nesnesini variable'a
# kaydedebiliriz.
#
# Böylece Python'un oluşturduğu hata mesajını görebiliriz.


# ============================================================
# 15 - INPUT İLE EXCEPTION
# ============================================================

text = input("Enter a number: ")

try:

    number = int(text)

except ValueError:

    print("Please enter a valid number")

else:

    print(f"Number: {number}")

# Kullanıcı sayı yerine başka bir şey girerse
# ValueError oluşur.
#
# Exception sayesinde programın kontrolünü
# kaybetmeyiz.


# ============================================================
# 16 - FUNCTION İÇİNDE EXCEPTION
# ============================================================

def convert_number(text):

    try:

        return int(text)

    except ValueError:

        return None


print(convert_number("100"))

print(convert_number("hello"))

# Exception handling function'ın içinde de yapılabilir.
#
# Burada geçersiz değer geldiğinde None döndürüyoruz.


# ============================================================
# 17 - RAISE
# ============================================================

def check_speed(speed):

    if speed < 0:

        raise ValueError("Speed cannot be negative")

    return speed


# raise ile kendi exception'ımızı oluşturabiliriz.
#
# Örneğin negatif motor hızı bizim function'ımız için
# geçersiz bir değer olabilir.


# ============================================================
# 18 - EXCEPTION'I GİZLEMEMEK
# ============================================================

# KÖTÜ:

try:

    number = int("hello")

except:

    pass

# pass hatayı tamamen görmezden gelir.
#
# Büyük robot projelerinde bu tehlikelidir.
#
# Örneğin bir sensörle ilgili problem oluştuğunda
# hatayı gizlersen sorunun nedenini bulmak zorlaşır.


# DAHA İYİ:

try:

    number = int("hello")

except ValueError:

    print("Invalid number")

# Beklediğimiz hatayı açıkça yakalamak daha iyidir.


# ============================================================
# 19 - VEX'TE EXCEPTION KULLANIMI
# ============================================================

# VEX'te try/except kullanımı normal Python
# programlarından biraz farklı düşünülmelidir.
#
# Robot:
#
#     motor
#     sensor
#     drivetrain
#     autonomous
#
# gibi gerçek zamanlı çalışan sistemlerden oluşur.
#
# Bir motor veya sensörle ilgili problemi
# try/except ile gizlemek genellikle doğru değildir.
#
# Öncelik:
#
#     1. Problemin nedenini bul
#     2. Kodu düzelt
#     3. Gerekirse exception handling kullan
#
# Exception handling daha çok:
#
#     veri dönüşümü
#     kullanıcı input'u
#     güvenli hesaplama
#     yardımcı function'lar
#
# gibi durumlarda kullanışlıdır.


# ============================================================
# 20 - KISA REFERANS + ANAHTAR BİLGİLER
# ============================================================

# try:
#     Hata çıkabilecek kodu çalıştırır.
#
# except:
#     Hata oluştuğunda çalışır.
#
# else:
#     Hata oluşmazsa çalışır.
#
# finally:
#     Her durumda çalışır.
#
# raise:
#     Elle exception oluşturur.
#
#
# En önemli exception'lar:
#
# ValueError
#     Değer uygun değil.
#
# TypeError
#     Veri türleri uygun değil.
#
# IndexError
#     Liste index'i bulunamadı.
#
# KeyError
#     Dictionary KEY'i bulunamadı.
#
# ZeroDivisionError
#     Sıfıra bölme yapıldı.
#
#
# Temel kullanım:
#
# try:
#
#     value = int("100")
#
# except ValueError:
#
#     print("Invalid")
#
#
# VEX açısından en önemli fikir:
#
# Exception handling, hataları gizlemek için değil,
# beklenebilecek hataları kontrollü şekilde yönetmek
# için kullanılmalıdır.






# ============================================================
# Ders 11 bitti, sıradaki konudan devam edebilirsiniz. 
# END OF 11 - EXCEPTIONS
# ============================================================

"""
BU DERSLE BERABER PYTHON BASICS KONUSU BITTI
Elbette değinilmemiş konular bulunmakta, fakat asıl amacımız VexV5 için bir kütüphane oluşturmak.
Bu nedenle bu konuların yeterli olacağını umuyorum.

Sıradaki konu;
VEX_FUNDAMENTALS

"""