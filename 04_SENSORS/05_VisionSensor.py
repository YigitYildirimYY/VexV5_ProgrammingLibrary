# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 05 - VISION SENSOR
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. VISION SENSOR NEDİR?
# ------------------------------------------------------------
#
# Vision Sensor, kamerayı kullanarak belirli renkleri veya
# renklerden oluşan belirli desenleri algılamamızı sağlar.
#
# Optical Sensor'dan temel farkı, sadece sensörün önündeki
# rengi ölçmek yerine görüntü içerisindeki nesnelerin
# konumunu ve boyutunu da takip edebilmesidir.
#
# Vision Sensor iki temel şeyle çalışır:
#
# Color Signature:
# Belirli bir rengi tanımlayan ayardır.
#
# Color Code:
# Birden fazla Color Signature'ın belirli bir düzende
# birleşimidir.
#
# Vision Sensor'ı kullanmadan önce bu imzaların Vision
# Utility'de oluşturulması gerekir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. VISION SENSOR TANIMLAMA
# ------------------------------------------------------------
#
# Vision Sensor'ı doğrudan bir Smart Port'a bağlayabiliriz.
#
# Brightness değeri kameranın kullandığı LED ışığının
# parlaklığıdır ve 1 ile 100 arasında olabilir.
#
# Burada henüz bir Signature eklemiyoruz. Signature'lar
# birazdan oluşturulacak.
# ------------------------------------------------------------

brain = Brain()

vision = Vision(Ports.PORT7, 50)


# ------------------------------------------------------------
# 3. COLOR SIGNATURE OLUŞTURMA
# ------------------------------------------------------------
#
# Vision Sensor'ın belirli bir rengi tanıyabilmesi için
# Color Signature oluşturulur.
#
# Signature() dokuz değer alır. Bu değerler Vision Utility'de
# oluşturulan signature ayarlarından gelir.
#
# Aşağıdaki değerler sadece örnek bir signature içindir.
# Kendi robotunda bunları Vision Utility'deki değerlerle
# değiştirmelisin.
# ------------------------------------------------------------

RED_BOX = Signature(
    1,
    10121,
    10757,
    10439,
    -1657,
    -1223,
    -1440,
    2.5,
    1
)


# ------------------------------------------------------------
# 4. COLOR CODE
# ------------------------------------------------------------
#
# Color Code, birden fazla Color Signature'ın belirli bir
# sırayla birleştirilmesiyle oluşturulur.
#
# Örneğin kırmızı + mavi şeklinde özel bir işaret
# tanımlanabilir.
#
# Bu derste yalnızca Color Signature kullanacağımız için
# burada Color Code oluşturmuyoruz.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 5. VISION SENSOR'A SIGNATURE EKLEME
# ------------------------------------------------------------
#
# Vision Sensor oluşturulurken Signature'ı constructor'a
# verebiliriz.
#
# Bu nedenle pratikte Vision Sensor'ı Signature ile birlikte
# tanımlamak daha kullanışlıdır.
# ------------------------------------------------------------

vision = Vision(Ports.PORT7, 50, RED_BOX)


# ------------------------------------------------------------
# 6. SENSOR BAĞLI MI?
# ------------------------------------------------------------
#
# installed(), Vision Sensor'ın V5 Brain'e bağlı olup
# olmadığını kontrol eder.
#
# True  -> bağlı
# False -> bağlı değil
# ------------------------------------------------------------

if vision.installed():
    brain.screen.print("Vision Sensor connected")
else:
    brain.screen.print("Vision Sensor not connected")


# ------------------------------------------------------------
# 7. TAKE_SNAPSHOT
# ------------------------------------------------------------
#
# take_snapshot(), Vision Sensor'ın kamerasından bir görüntü
# alır ve seçtiğimiz Signature ile eşleşen nesneleri döndürür.
#
# Dönen nesneler en büyükten en küçüğe doğru sıralanır.
#
# İlk nesne:
#
#     red_objects[0]
#
# olur.
# ------------------------------------------------------------

red_objects = vision.take_snapshot(RED_BOX)


# ------------------------------------------------------------
# 8. EXISTS
# ------------------------------------------------------------
#
# exists, ilgili sırada gerçekten bir nesne olup olmadığını
# kontrol eder.
#
# Nesne varsa True, yoksa False olur.
#
# Bu kontrolü yapmadan centerX, width gibi özellikleri
# kullanmak hata oluşturabilir.
# ------------------------------------------------------------

if red_objects[0].exists:
    brain.screen.print("Red object detected")
else:
    brain.screen.print("No red object")


# ------------------------------------------------------------
# 9. CENTER X VE CENTER Y
# ------------------------------------------------------------
#
# centerX ve centerY, algılanan nesnenin görüntü içindeki
# merkez koordinatlarını verir.
#
# Vision Sensor'ın çözünürlüğü 316 x 212 pikseldir.
#
# centerX:
# 0  → görüntünün solu
# 316 → görüntünün sağı
#
# centerY:
# 0  → görüntünün üstü
# 212 → görüntünün altı
# ------------------------------------------------------------

if red_objects[0].exists:

    x = red_objects[0].centerX
    y = red_objects[0].centerY

    brain.screen.print(x)
    brain.screen.print(y)


# ------------------------------------------------------------
# 10. WIDTH VE HEIGHT
# ------------------------------------------------------------
#
# width ve height, algılanan nesnenin görüntüde kapladığı
# alanın genişliğini ve yüksekliğini piksel cinsinden verir.
#
# Nesne kameraya yaklaştıkça genellikle daha büyük görünür.
# Bu yüzden bu değerler nesnenin yaklaşık olarak ne kadar
# büyük göründüğünü takip etmek için kullanılabilir.
# ------------------------------------------------------------

if red_objects[0].exists:

    width = red_objects[0].width
    height = red_objects[0].height

    brain.screen.print(width)
    brain.screen.print(height)


# ------------------------------------------------------------
# 11. LARGEST_OBJECT
# ------------------------------------------------------------
#
# take_snapshot() birden fazla nesne bulabilir.
#
# largest_object(), son snapshot'taki en büyük nesneyi
# doğrudan seçmemizi sağlar.
#
# Böylece:
#
# red_objects[0]
#
# kullanmak yerine:
#
# vision.largest_object()
#
# kullanabiliriz.
# ------------------------------------------------------------

red_objects = vision.take_snapshot(RED_BOX)

if red_objects[0].exists:

    largest = vision.largest_object()

    brain.screen.print(largest.centerX)
    brain.screen.print(largest.centerY)


# ------------------------------------------------------------
# 12. ORIGIN X VE ORIGIN Y
# ------------------------------------------------------------
#
# originX ve originY, algılanan nesnenin görüntüdeki
# bounding box'ının sol üst köşesinin koordinatlarını verir.
#
# centerX ve centerY nesnenin merkezini,
# originX ve originY ise kutunun başlangıç noktasını gösterir.
# ------------------------------------------------------------

if red_objects[0].exists:

    x = red_objects[0].originX
    y = red_objects[0].originY

    brain.screen.print(x)
    brain.screen.print(y)


# ------------------------------------------------------------
# 13. ANGLE
# ------------------------------------------------------------
#
# angle, algılanan bir Color Code'un görüntüdeki dönüş
# açısını derece cinsinden verir.
#
# Bu özellik özellikle Color Code kullanırken işe yarar.
# ------------------------------------------------------------

if red_objects[0].exists:

    angle = red_objects[0].angle

    brain.screen.print(angle)


# ------------------------------------------------------------
# 14. AUTONOMOUS'TA KULLANIM
# ------------------------------------------------------------
#
# Vision Sensor autonomous programlarda robotun belirli bir
# renkteki nesneyi görmesine ve onun görüntüdeki konumuna
# göre hareket etmesine yardımcı olabilir.
#
# Örneğin nesne görüntünün solundaysa robot sola,
# sağındaysa sağa dönerek nesneyi kameranın ortasına
# getirebilir.
#
# Burada Vision Sensor sadece görüntüden bilgi sağlar.
# Motorların ne yapacağını program belirler.
# ------------------------------------------------------------


# ============================================================
# Ders 05 bitti, bir sonraki derse geçin.
# END OF 05 - VISION SENSOR
# ============================================================