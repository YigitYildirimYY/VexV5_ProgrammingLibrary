# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 03 - DISTANCE SENSOR
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. DISTANCE SENSOR NEDİR?
# ------------------------------------------------------------
#
# Distance Sensor, önündeki en yakın algılanabilir nesne ile
# sensör arasındaki mesafeyi ölçer.
#
# Özellikle autonomous programlarda nesne algılamak, bir
# duvara yaklaşmak veya belirli bir mesafede durmak için
# kullanılır.
#
# Sensörün çalışma aralığı 20 mm ile 2000 mm arasındadır.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. SENSOR TANIMLAMA
# ------------------------------------------------------------

brain = Brain()

distance = Distance(Ports.PORT7)


# ------------------------------------------------------------
# 3. OBJECT_DISTANCE
# ------------------------------------------------------------
#
# object_distance() en yakın algılanan nesnenin sensöre
# olan uzaklığını verir.
#
# Birim olarak MM veya INCHES kullanılabilir.
# ------------------------------------------------------------

distance_mm = distance.object_distance(MM)

brain.screen.print(distance_mm)


distance_inches = distance.object_distance(INCHES)

brain.screen.print(distance_inches)


# ------------------------------------------------------------
# 4. IS_OBJECT_DETECTED
# ------------------------------------------------------------
#
# is_object_detected() sensörün şu anda bir nesne algılayıp
# algılamadığını kontrol eder.
#
# Sonuç True veya False olur.
# ------------------------------------------------------------

if distance.is_object_detected():
    brain.screen.print("Object detected")
else:
    brain.screen.print("No object detected")


# ------------------------------------------------------------
# 5. OBJECT_SIZE
# ------------------------------------------------------------
#
# object_size(), algılanan nesnenin sensörün görüş alanında
# kapladığı alana göre boyutunu tahmin eder.
#
# Sonuç NONE, SMALL, MEDIUM veya LARGE olabilir.
#
# Bu gerçek nesnenin fiziksel boyutunu kesin olarak ölçmek
# anlamına gelmez; sensörün yaptığı bir tahmindir.
# ------------------------------------------------------------

size = distance.object_size()

brain.screen.print(size)


# ------------------------------------------------------------
# 6. OBJECT_VELOCITY
# ------------------------------------------------------------
#
# object_velocity(), algılanan nesnenin sensöre göre ne kadar
# hızlı yaklaştığını veya uzaklaştığını verir.
#
# Sonuç metre/saniye (m/s) cinsindendir.
#
# Bu değer nesnenin sensöre göre bağıl hızıdır.
# ------------------------------------------------------------

velocity = distance.object_velocity()

brain.screen.print(velocity)


# ------------------------------------------------------------
# 7. MESAFEYE GÖRE KARAR VERME
# ------------------------------------------------------------
#
# Sensörden aldığımız mesafeyi normal bir koşul içinde
# kullanabiliriz.
#
# Örneğin nesne 200 mm'den daha yakınsa bir işlem
# gerçekleştirebiliriz.
# ------------------------------------------------------------

if distance.is_object_detected():

    if distance.object_distance(MM) < 200:
        brain.screen.print("Object is close")


# ------------------------------------------------------------
# 8. BASİT BİR KONTROL ÖRNEĞİ
# ------------------------------------------------------------
#
# Aşağıdaki örnekte robotun hareketini kontrol etmiyoruz.
# Sadece sensörün ölçümünü takip ediyoruz.
#
# Bir nesne algılandığında ve nesne 100 mm'den daha yakın
# olduğunda döngü sona erer.
# ------------------------------------------------------------

while True:

    if distance.is_object_detected():

        current_distance = distance.object_distance(MM)

        if current_distance <= 100:
            break

    wait(10, MSEC)


# ------------------------------------------------------------
# 9. AUTONOMOUS'TA KULLANIM
# ------------------------------------------------------------
#
# Distance Sensor autonomous programlarda örneğin robotun
# bir duvara veya nesneye yaklaşırken belirli bir mesafede
# durmasını sağlamak için kullanılabilir.
#
# Önemli nokta:
#
# Distance Sensor robotun sahadaki X ve Y koordinatını
# doğrudan vermez.
#
# Sadece sensör ile algılanan nesne arasındaki mesafeyi verir.
#
# Robotun konumunu hesaplamak için GPS, Rotation Sensor,
# IMU ve odometry gibi başka sistemlerden yararlanabiliriz.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 10. SENSORUN SINIRLAMALARI
# ------------------------------------------------------------
#
# Distance Sensor'ın ölçüm aralığı 20 mm - 2000 mm'dir.
#
# 200 mm'nin altında yaklaşık ±15 mm doğruluk,
# 200 mm'nin üzerinde ise yaklaşık %5 doğruluk belirtilmiştir.
#
# Bu nedenle gerçek robotta sensörden gelen değerler
# küçük miktarlarda değişebilir.
#
# Örneğin:
#
# 200
# 202
# 198
# 201
#
# gibi değerler görmek normal olabilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 11. CHANGED
# ------------------------------------------------------------
#
# changed(), Distance Sensor'ın değeri değiştiğinde belirli
# bir fonksiyonun çalıştırılmasını sağlar.
#
# Bu konu callback mantığıyla ilgili olduğu için burada
# sadece API'sini tanıyoruz.
# ------------------------------------------------------------

def distance_changed():
    brain.screen.print("Distance changed")


distance.changed(distance_changed)


# ============================================================
# Ders 03 bitti, bir sonraki derse geçin.
# END OF 03 - DISTANCE SENSOR
# ============================================================