# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 08 - SENSOR DEBUGGING
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. SENSOR DEBUGGING NEDİR?
# ------------------------------------------------------------
#
# Robot kodunda sensörlerden gelen verileri doğrudan görmek,
# sensörün gerçekten ne yaptığını anlamamızı sağlar.
#
# Örneğin robotun neden doğru dönmediğini anlamaya çalışırken
# sadece motor koduna bakmak yerine IMU'nun heading değerini
# kontrol edebiliriz.
#
# Debugging sırasında temel olarak şu sorulara bakarız:
#
# - Sensör doğru bağlanmış mı?
# - Doğru port kullanılıyor mu?
# - Sensörden gerçekten veri geliyor mu?
# - Gelen değer beklediğimiz aralıkta mı?
# - Sensör hareket ettiğinde değer değişiyor mu?
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. BRAIN SCREEN İLE DEĞER GÖRÜNTÜLEME
# ------------------------------------------------------------
#
# Bir sensör değerini kontrol etmenin en basit yolu Brain
# Screen'e yazdırmaktır.
# ------------------------------------------------------------

brain = Brain()

imu = Inertial(Ports.PORT7)

brain.screen.print(imu.heading(DEGREES))


# ------------------------------------------------------------
# 3. DEĞERİ SÜREKLİ İZLEME
# ------------------------------------------------------------
#
# Sensör hareket ettikçe değerinin nasıl değiştiğini görmek
# için değeri sürekli okuyabiliriz.
# ------------------------------------------------------------

while True:

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    brain.screen.print(imu.heading(DEGREES))

    wait(100, MSEC)


# ------------------------------------------------------------
# 4. BİRDEN FAZLA SENSÖRÜ KONTROL ETME
# ------------------------------------------------------------
#
# Robotumuzda birden fazla sensör varsa aynı anda birkaç
# değeri ekrana yazdırabiliriz.
#
# Örneğin IMU ve Rotation Sensor'ı birlikte izlemek,
# odometry ile ilgili problemleri araştırırken çok faydalıdır.
# ------------------------------------------------------------

imu = Inertial(Ports.PORT7)
rotation = Rotation(Ports.PORT8)

while True:

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    brain.screen.print(imu.heading(DEGREES))

    brain.screen.next_row()

    brain.screen.print(rotation.position(DEGREES))

    wait(100, MSEC)


# ------------------------------------------------------------
# 5. PORT KONTROLÜ
# ------------------------------------------------------------
#
# Sensör doğru çalışmıyorsa kontrol edilmesi gereken ilk
# şeylerden biri port numarasıdır.
#
# Örneğin sensör fiziksel olarak PORT7'deyse kodda da:
#
#     Inertial(Ports.PORT7)
#
# kullanılmalıdır.
#
# Yanlış port kullanılırsa sensör verisi beklediğimiz gibi
# çalışmayabilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 6. SENSOR HAREKET EDERKEN DEĞER DEĞİŞİYOR MU?
# ------------------------------------------------------------
#
# Bir sensörün çalışıp çalışmadığını anlamanın basit
# yöntemlerinden biri, fiziksel olarak sensörü veya bağlı
# olduğu parçayı hareket ettirirken değerini izlemektir.
#
# Örneğin Rotation Sensor için:
#
#     rotation.position(DEGREES)
#
# değeri sensör döndükçe değişmelidir.
#
# IMU için robotu kontrollü şekilde döndürdüğümüzde:
#
#     imu.heading(DEGREES)
#
# değeri değişmelidir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 7. DEĞERLER MANTIKLI MI?
# ------------------------------------------------------------
#
# Sensörden veri gelmesi tek başına yeterli değildir.
# Gelen değerin mantıklı olup olmadığına da bakmalıyız.
#
# Örneğin robot sabit dururken heading'in sürekli çok büyük
# miktarda değişmesi beklenmez.
#
# Benzer şekilde Rotation Sensor fiziksel olarak hareket
# etmiyorsa position değerinin sürekli artması normal değildir.
#
# Böyle bir durumda:
#
# - Port
# - Sensör montajı
# - Kalibrasyon
# - Kod
# - Sensör yönü
#
# gibi şeyleri kontrol ederiz.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 8. SENSOR DEĞERİNİ MOTOR KODUNDAN AYIRMAK
# ------------------------------------------------------------
#
# Bir robot doğru hareket etmiyorsa problemi doğrudan motor
# kodunda aramak yerine önce sensörün doğru veri verip
# vermediğini kontrol etmek daha mantıklıdır.
#
# Örneğin:
#
# IMU → heading'i doğru veriyor mu?
# Rotation Sensor → dönüşü doğru ölçüyor mu?
# Distance Sensor → mesafeyi doğru okuyor mu?
#
# Sensör verisi doğruysa daha sonra motor ve kontrol
# algoritmasını incelemeye geçebiliriz.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 9. SIMPLE SENSOR TEST
# ------------------------------------------------------------
#
# Yeni bir sensör taktığımızda önce küçük bir test programı
# yazmak iyi bir alışkanlıktır.
#
# İlk aşamada robotu hareket ettirmek yerine sadece sensörün
# değerlerini okumak daha güvenlidir ve problemi daha kolay
# bulmamızı sağlar.
# ------------------------------------------------------------

distance = Distance(Ports.PORT9)

while True:

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    if distance.is_object_detected():

        brain.screen.print(distance.object_distance(MM))

    else:

        brain.screen.print("No object")

    wait(100, MSEC)


# ------------------------------------------------------------
# 10. DEBUGGING İÇİN TEMEL MANTIK
# ------------------------------------------------------------
#
# Sensörle ilgili bir problem olduğunda şu sırayla ilerlemek
# iyi bir yöntemdir:
#
# 1. Sensör fiziksel olarak doğru bağlandı mı?
# 2. Kodda doğru port kullanıldı mı?
# 3. Sensör tanımlaması doğru mu?
# 4. Sensörden değer okuyabiliyor muyuz?
# 5. Değer fiziksel hareketle değişiyor mu?
# 6. Gelen değer mantıklı mı?
# 7. Ancak bundan sonra motor veya autonomous kodunu
#    incelemeli miyiz?
#
# Böylece sensör problemi ile kontrol algoritması problemini
# birbirine karıştırmamış oluruz.
# ------------------------------------------------------------


# ============================================================
# Ders 08 bitti, bir sonraki derse geçin.
# END OF 08 - SENSOR DEBUGGING
# ============================================================