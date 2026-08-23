# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 00 - PYTHON BASICS
# Yiğit YILDIRIM
# 03 - CONDITIONS
# ============================================================

# ============================================================
# 1. CONDITIONS NEDİR?
# ============================================================
#
# Condition (koşul), programın belirli bir durumun doğru
# veya yanlış olup olmadığını kontrol etmesini sağlar.
#
# Robot programlamada bilgisayarın sadece sırayla komut
# çalıştırması çoğu zaman yeterli değildir.
#
# Örneğin:
#
#     Eğer bir durum gerçekleşirse bir şey yap.
#     Değilse başka bir şey yap.
#
# Python'da bunu yapmak için temel olarak:
#
#     if
#     elif
#     else
#
# kullanılır.
#
# Conditions konusu comparison ve logical operatorlerle
# doğrudan bağlantılıdır.
#
# Örneğin:
#
#     speed > 50
#
# ifadesinin sonucu:
#
#     True
#
# veya:
#
#     False
#
# olabilir.


# ============================================================
# 2. IF
# ============================================================
#
# "if", bir koşul True olduğunda belirli kodların
# çalışmasını sağlar.
#
# Temel yapı:
#
#     if condition:
#         code
#
# Dikkat:
#
# if satırının sonunda ":" bulunur.
#
# if'in altında bulunan kod girintili (indented) olmalıdır.


# ============================================================
# 3. BASİT IF ÖRNEĞİ
# ============================================================

speed = 80

if speed > 50:
    print("Speed is greater than 50")


# Burada:
#
# speed > 50
#
# koşuludur.
#
# speed = 80 olduğu için:
#
# 80 > 50
#
# True olur.
#
# Dolayısıyla print() çalışır.


# ============================================================
# 4. KOŞUL FALSE OLURSA
# ============================================================

speed = 30

if speed > 50:
    print("Speed is greater than 50")


# Burada:
#
# 30 > 50
#
# False olduğu için print() çalışmaz.
#
# Program hata vermez.
# Sadece if bloğunun içindeki kod çalıştırılmaz.


# ============================================================
# 5. INDENTATION
# ============================================================
#
# Python'da girinti çok önemlidir.
#
# if'in içine ait olan kodlar girintili yazılır.

speed = 80

if speed > 50:
    print("Speed is high")
    print("This line is also inside the if")


print("This line is outside the if")


# İlk iki print() yalnızca koşul True olduğunda çalışır.
#
# Son print() ise her durumda çalışır.


# ============================================================
# 6. IF + COMPARISON OPERATORS
# ============================================================
#
# if ile comparison operatorler çok sık birlikte kullanılır.

temperature = 40

if temperature > 30:
    print("Temperature is high")


# Kullanılabilecek comparison operatorler:
#
# ==
# !=
# >
# <
# >=
# <=


# ============================================================
# 7. EŞİTLİK KONTROLÜ
# ============================================================

speed = 100

if speed == 100:
    print("Maximum speed")


# speed = 100 olduğu için koşul True'dur.


# ============================================================
# 8. EŞİT OLMAMA KONTROLÜ
# ============================================================

speed = 80

if speed != 100:
    print("Speed is not maximum")


# ============================================================
# 9. BÜYÜKLÜK KONTROLÜ
# ============================================================

distance = 150

if distance > 100:
    print("Distance is greater than 100")


# ============================================================
# 10. KÜÇÜKLÜK KONTROLÜ
# ============================================================

distance = 50

if distance < 100:
    print("Distance is less than 100")


# ============================================================
# 11. BÜYÜK VEYA EŞİT
# ============================================================

score = 80

if score >= 70:
    print("Passed")


# ============================================================
# 12. KÜÇÜK VEYA EŞİT
# ============================================================

speed = 100

if speed <= 100:
    print("Speed is within the limit")


# ============================================================
# 13. IF + BOOLEAN
# ============================================================
#
# if doğrudan boolean değerle de kullanılabilir.

robot_ready = True

if robot_ready:
    print("Robot is ready")


# robot_ready False olursa:

robot_ready = False

if robot_ready:
    print("Robot is ready")


# Bu sefer print() çalışmaz.


# ============================================================
# 14. ELSE
# ============================================================
#
# "else", if koşulu False olduğunda çalışır.
#
# Temel yapı:
#
#     if condition:
#         ...
#     else:
#         ...
#
# Yani:
#
# if -> koşul True ise
# else -> koşul False ise


# ============================================================
# 15. BASİT IF / ELSE
# ============================================================

speed = 40

if speed > 50:
    print("Fast")

else:
    print("Slow")


# speed > 50 False olduğu için:
#
# Slow
#
# yazdırılır.


# ============================================================
# 16. IF / ELSE MANTIĞI
# ============================================================
#
# Aşağıdaki iki durumdan yalnızca biri çalışır.

robot_ready = True

if robot_ready:
    print("Robot can start")

else:
    print("Robot cannot start")


# robot_ready = True:
#
# if çalışır.
#
# robot_ready = False:
#
# else çalışır.


# ============================================================
# 17. VEX'TE BASİT KOŞUL
# ============================================================
#
# Henüz VEX sensorlerini öğrenmediğimiz için gerçek sensor
# nesneleri kullanmıyoruz.
#
# Ancak bir sensor değerinin bir değişkende tutulduğunu
# varsayabiliriz.

distance = 150

if distance < 200:
    print("Object is close")

else:
    print("Object is far")


# Bu yapı ileride gerçek bir Distance Sensor değeriyle
# kullanılabilir.


# ============================================================
# 18. ELIF
# ============================================================
#
# "elif", "else if" anlamına gelir.
#
# Birden fazla farklı durumu kontrol etmek istediğimizde
# kullanılır.
#
# Temel yapı:
#
#     if condition1:
#         ...
#
#     elif condition2:
#         ...
#
#     else:
#         ...


# ============================================================
# 19. BASİT ELIF
# ============================================================

speed = 70

if speed > 80:
    print("Fast")

elif speed > 50:
    print("Medium")

else:
    print("Slow")


# speed = 70 olduğu için:
#
# speed > 80
# -> False
#
# speed > 50
# -> True
#
# Sonuç:
#
# Medium


# ============================================================
# 20. BİRDEN FAZLA ELIF
# ============================================================

score = 85

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

elif score >= 60:
    print("D")

else:
    print("F")


# score = 85 olduğu için:
#
# score >= 90 -> False
# score >= 80 -> True
#
# Sonuç:
#
# B


# ============================================================
# 21. ELIF SIRASININ ÖNEMİ
# ============================================================
#
# Python yukarıdan aşağıya doğru kontrol eder.
#
# İlk True olan koşulun bloğunu çalıştırır.
#
# Örneğin:

speed = 90

if speed > 50:
    print("Above 50")

elif speed > 80:
    print("Above 80")

else:
    print("50 or below")


# Burada:
#
# speed > 50
#
# zaten True olduğu için ilk blok çalışır.
#
# "Above 80" yazdırılmaz.
#
# Bu nedenle koşulların sırası önemlidir.


# ============================================================
# 22. DOĞRU SIRALAMA
# ============================================================
#
# Daha spesifik koşulu önce yazmak çoğu durumda daha
# mantıklıdır.

speed = 90

if speed > 80:
    print("Very fast")

elif speed > 50:
    print("Fast")

else:
    print("Slow")


# Sonuç:
#
# Very fast


# ============================================================
# 23. IF / ELIF / ELSE İLE ARALIKLAR
# ============================================================
#
# Bir değeri farklı aralıklara ayırabiliriz.

speed = 65

if speed >= 80:
    print("High")

elif speed >= 50:
    print("Medium")

else:
    print("Low")


# speed = 65:
#
# 65 >= 80 -> False
# 65 >= 50 -> True
#
# Sonuç:
#
# Medium


# ============================================================
# 24. LOGICAL OPERATORS İLE CONDITIONS
# ============================================================
#
# Bir koşulun içinde and, or ve not kullanabiliriz.
#
# Örneğin:

speed = 70
distance = 100

if speed > 50 and distance < 200:
    print("Condition satisfied")


# İki koşul da True olmalıdır.


# ============================================================
# 25. AND İLE IF
# ============================================================

robot_ready = True
battery_ok = True

if robot_ready and battery_ok:
    print("Robot can start")


# Burada:
#
# robot_ready -> True
# battery_ok  -> True
#
# True and True
# -> True


# Eğer:

battery_ok = False

if robot_ready and battery_ok:
    print("Robot can start")

else:
    print("Robot cannot start")


# Sonuç:
#
# Robot cannot start


# ============================================================
# 26. OR İLE IF
# ============================================================
#
# "or" kullanıldığında koşullardan en az birinin True olması
# yeterlidir.

button_a = False
button_b = True

if button_a or button_b:
    print("A button is active")


# False or True
# -> True


# ============================================================
# 27. NOT İLE IF
# ============================================================

robot_ready = False

if not robot_ready:
    print("Robot is not ready")


# robot_ready = False
#
# not False
# -> True


# ============================================================
# 28. KARMAŞIK KOŞULLAR
# ============================================================
#
# Bir if içinde birden fazla logical operator kullanılabilir.

robot_ready = True
battery_ok = True
autonomous_mode = True

if robot_ready and battery_ok and autonomous_mode:
    print("Autonomous can start")


# Üç koşulun da True olması gerekir.


# ============================================================
# 29. PARANTEZLİ KOŞULLAR
# ============================================================
#
# Karmaşık koşullarda parantez kullanmak hem okunabilirliği
# hem de kontrolü artırır.

button_a = False
button_b = True
robot_ready = True

if robot_ready and (button_a or button_b):
    print("Action allowed")


# Önce:
#
# button_a or button_b
#
# değerlendirilir.
#
# Sonra:
#
# robot_ready and result
#
# değerlendirilir.


# ============================================================
# 30. NESTED IF
# ============================================================
#
# Bir if'in içinde başka bir if bulunabilir.
#
# Buna nested if denir.

robot_ready = True
battery_ok = True

if robot_ready:

    if battery_ok:
        print("Robot can start")


# Burada önce robot_ready kontrol edilir.
#
# True ise ikinci if'e geçilir.
#
# Daha sonra battery_ok kontrol edilir.


# ============================================================
# 31. NESTED IF + ELSE
# ============================================================

robot_ready = True
battery_ok = False

if robot_ready:

    if battery_ok:
        print("Robot can start")

    else:
        print("Battery is not OK")

else:

    print("Robot is not ready")


# Bu yapı çalışır ancak çok fazla nested if kullanmak
# programın okunmasını zorlaştırabilir.
#
# İleride aynı mantığı daha temiz şekilde yazmanın
# yöntemlerini göreceğiz.


# ============================================================
# 32. KOŞUL İÇİNDE HESAPLAMA
# ============================================================
#
# if'in içinde doğrudan matematiksel bir ifade kullanabiliriz.

speed = 80

if speed + 10 > 100:
    print("Speed would exceed limit")


# Python önce:
#
# speed + 10
#
# hesaplar.
#
# Sonra:
#
# > 100
#
# kontrol edilir.


# ============================================================
# 33. MODULO İLE CONDITION
# ============================================================
#
# Modulo sonucu da koşul olarak kullanılabilir.

number = 10

if number % 2 == 0:
    print("Even number")

else:
    print("Odd number")


# Burada:
#
# number % 2
#
# hesaplanır.
#
# Sonra:
#
# == 0
#
# kontrol edilir.


# ============================================================
# 34. RANGE CHECK
# ============================================================
#
# Bir değerin iki sınır arasında olup olmadığını kontrol
# edebiliriz.

speed = 70

if speed >= 0 and speed <= 100:
    print("Valid speed")

else:
    print("Invalid speed")


# Burada iki koşul da True olmalıdır:
#
# speed >= 0
# speed <= 100


# ============================================================
# 35. VEX MOTOR HIZI KONTROLÜ
# ============================================================
#
# Gerçek bir motor komutu vermeden önce bir hız değerini
# kontrol edebiliriz.

motor_speed = 80

if motor_speed > 100:
    print("Invalid speed")

else:
    print("Speed is valid")


# Burada motor_speed 100'den büyük olmadığı için:
#
# Speed is valid
#
# yazdırılır.


# ============================================================
# 36. NEGATİF DEĞERLERLE CONDITION
# ============================================================

motor_speed = -50

if motor_speed < 0:
    print("Motor is commanded in reverse")

else:
    print("Motor is commanded forward")


# Burada:
#
# -50 < 0
#
# True'dur.


# ============================================================
# 37. TOLERANCE MANTIĞINA GİRİŞ
# ============================================================
#
# Bu konu ileride kontrol sistemlerinde ayrıntılı olarak
# ele alınacaktır.
#
# Burada sadece conditions kullanımını görmek için basit
# bir örnek veriyoruz.

target = 100
current = 97

error = target - current

if error >= -5 and error <= 5:
    print("Close enough")

else:
    print("Not close enough")


# error:
#
# 100 - 97 = 3
#
# 3 değeri -5 ile 5 arasında olduğu için:
#
# Close enough


# ============================================================
# 38. ABS() İLE CONDITION
# ============================================================
#
# abs() bir değerin mutlak değerini verir.
#
# Burada condition içinde kullanılabilir.

error = -3

if abs(error) <= 5:
    print("Close enough")

else:
    print("Too far")


# Bu örnekte:
#
# abs(-3) = 3
#
# 3 <= 5
#
# True


# Not:
#
# abs() fonksiyonunu burada sadece condition içinde
# kullanıldığını göstermek için görüyoruz.
# Fonksiyonlar konusu ayrı bir derste ayrıntılı işlenecek.


# ============================================================
# 39. BOOLEAN DEĞERLERİN DOĞRUDAN KULLANILMASI
# ============================================================

autonomous_running = True

if autonomous_running:
    print("Autonomous is running")

else:
    print("Autonomous is not running")


# Boolean değişkenlerde == True yazmak çoğu zaman gereksizdir.
#
# Örneğin:

if autonomous_running:
    print("Running")


# şu kullanımdan daha temizdir:

if autonomous_running == True:
    print("Running")


# İkincisi çalışır ancak ilki daha yaygın ve okunabilirdir.


# ============================================================
# 40. FALSE DURUMUNUN KONTROLÜ
# ============================================================

autonomous_running = False

if not autonomous_running:
    print("Autonomous is not running")


# "not" burada False değerini True'ya çevirir.


# ============================================================
# 41. BİRDEN FAZLA DURUM
# ============================================================
#
# Bir robotun farklı durumları olabilir.
#
# Örneğin:

mode = "autonomous"

if mode == "autonomous":
    print("Autonomous mode")

elif mode == "driver":
    print("Driver mode")

else:
    print("Unknown mode")


# Bu yapı ileride state machine mantığına temel oluşturur.
#
# Ancak state machine'i henüz burada öğrenmiyoruz.


# ============================================================
# 42. STRING CONDITION
# ============================================================

robot_mode = "autonomous"

if robot_mode == "autonomous":
    print("Running autonomous")


# Stringler de comparison operatorleriyle karşılaştırılabilir.


# ============================================================
# 43. BİR KOŞULDA BİRDEN FAZLA KARŞILAŞTIRMA
# ============================================================

speed = 70
distance = 150

if speed >= 50 and speed <= 100 and distance < 200:
    print("All conditions are satisfied")


# Burada üç ayrı comparison vardır:
#
# speed >= 50
# speed <= 100
# distance < 200
#
# "and" hepsini birleştirir.


# ============================================================
# 44. OR + AND
# ============================================================
#
# "and" ve "or" aynı koşul içerisinde kullanılabilir.

button_a = False
button_b = True
robot_ready = True

if robot_ready and (button_a or button_b):
    print("Robot can perform action")


# Burada:
#
# button_a or button_b
#
# önce değerlendirilir.
#
# Daha sonra:
#
# robot_ready and result
#
# değerlendirilir.


# ============================================================
# 45. IF / ELIF / ELSE İLE ROBOT DURUMU
# ============================================================
#
# Basit bir robot durum sistemi oluşturalım.

battery = 75

if battery >= 80:
    print("Battery: High")

elif battery >= 40:
    print("Battery: Medium")

elif battery >= 20:
    print("Battery: Low")

else:
    print("Battery: Critical")


# battery = 75 olduğu için:
#
# Battery: Medium


# ============================================================
# 46. KOŞULLARIN SIRASI
# ============================================================
#
# Bu örnek özellikle önemlidir.

battery = 90

if battery >= 20:
    print("Battery above 20")

elif battery >= 80:
    print("Battery above 80")


# İlk koşul True olduğu için:
#
# Battery above 20
#
# yazdırılır.
#
# İkinci koşul hiç kontrol edilmez.
#
# Bu nedenle daha özel durumlar önce yazılmalıdır.


# Doğru kullanım:

battery = 90

if battery >= 80:
    print("Battery above 80")

elif battery >= 20:
    print("Battery above 20")


# Sonuç:
#
# Battery above 80


# ============================================================
# 47. IF BLOĞUNDA BİRDEN FAZLA KOMUT
# ============================================================
#
# Bir condition True olduğunda yalnızca bir komut değil,
# birden fazla komut çalıştırabiliriz.

speed = 80

if speed > 50:
    print("Speed is high")
    print("Warning")
    print("Check robot")


# Üç satırın tamamı if bloğunun içindedir.


# ============================================================
# 48. ELSE BLOĞUNDA BİRDEN FAZLA KOMUT
# ============================================================

speed = 30

if speed > 50:
    print("Speed is high")

else:
    print("Speed is low")
    print("Robot can accelerate")


# ============================================================
# 49. CONDITIONS VE PROGRAM AKIŞI
# ============================================================
#
# Şu ana kadar Python kodları genellikle yukarıdan aşağıya
# sırayla çalışıyordu.
#
# Conditions ile programın akışını değiştirebiliriz.
#
# Örneğin:

number = 10

print("Start")

if number > 5:
    print("Number is greater than 5")

print("End")


# Program:
#
# Start
# Number is greater than 5
# End
#
# şeklinde ilerler.


# Eğer:

number = 3

print("Start")

if number > 5:
    print("Number is greater than 5")

print("End")


# Bu durumda:
#
# Start
# End
#
# yazdırılır.


# ============================================================
# 50. VEX PROGRAMLAMADA CONDITIONS'IN ÖNEMİ
# ============================================================
#
# Conditions ileride robotun karar vermesini sağlayacak.
#
# Örneğin:
#
# Bir butona basıldı mı?
# Bir sensor belirli değerin altında mı?
# Robot hazır mı?
# Bir hedefe ulaşıldı mı?
# Bir mekanizma aktif mi?
# Bir işlem tamamlandı mı?
#
# gibi durumların hepsi condition kullanılarak kontrol
# edilebilir.
#
# Ancak bu dosyada henüz controller veya sensor API'lerini
# öğrenmiyoruz.
#
# Önce Python'daki condition mantığını sağlamlaştırıyoruz.



# ============================================================
# 61. ÖNEMLİ KURALLAR
# ============================================================
#
# 1.
# if satırının sonunda ":" kullanılır.
#
#
# 2.
# if bloğunun içindeki kodlar girintili olmalıdır.
#
#
# 3.
# "==" karşılaştırma yapar.
#
# "=" değer atar.
#
#
# 4.
# elif yalnızca if'ten sonra kullanılabilir.
#
#
# 5.
# else en sonda bulunur.
#
#
# 6.
# İlk True olan if/elif bloğu çalışır.
#
#
# 7.
# else, önceki koşulların hiçbiri True olmadığında çalışır.
#
#
# 8.
# and, or ve not koşulları birleştirmek için kullanılabilir.


# ============================================================
# 62. ÖZET
# ============================================================
#
# IF:
#
# Bir koşul True olduğunda kod çalıştırır.
#
#
# ELSE:
#
# Hiçbir if/elif koşulu True olmadığında çalışır.
#
#
# ELIF:
#
# Birden fazla alternatif koşul oluşturmamızı sağlar.
#
#
# AND:
#
# Tüm koşullar True olmalıdır.
#
#
# OR:
#
# En az bir koşul True olmalıdır.
#
#
# NOT:
#
# Boolean değeri tersine çevirir.
#
#
# Conditions ile birlikte sık kullanılan operatorler:
#
# ==
# !=
# >
# <
# >=
# <=
#
# Ayrıca:
#
# if
# elif
# else
#
# Python programlarının karar verme mekanizmasının temelini
# oluşturur.




# ============================================================
# Ders 03 bitti, sıradaki derse geçebilirsiniz.
# END OF 03 - CONDITIONS
# ============================================================