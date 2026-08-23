# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 06 - AI VISION SENSOR
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. AI VISION SENSOR NEDİR?
# ------------------------------------------------------------
#
# AI Vision Sensor, kameradan aldığı görüntüyü kullanarak
# nesneleri, renkleri ve AprilTag'leri algılayabilen gelişmiş
# bir görüntü sensörüdür.
#
# Normal Vision Sensor'dan en önemli farkı, hazır AI
# sınıflandırmalarını da kullanabilmesidir.
#
# Kullanım alanları:
# - Nesne tanıma
# - Renk algılama
# - AprilTag algılama
# - Nesnenin görüntüdeki konumunu bulma
# - Autonomous'ta görsel hedef takibi
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. SENSOR TANIMLAMA
# ------------------------------------------------------------
#
# AI Vision Sensor bir Smart Port'a bağlanır.
#
# Aşağıdaki örnekte sensöre yalnızca AI ile algılanabilen
# nesneleri ve AprilTag'leri takip etmesini söylüyoruz.
# ------------------------------------------------------------

brain = Brain()

ai_vision = AiVision(
    Ports.PORT7,
    AiVision.ALL_AIOBJS,
    AiVision.ALL_TAGS
)


# ------------------------------------------------------------
# 3. AI OBJECTS ALGILAMA
# ------------------------------------------------------------
#
# ALL_AIOBJS, sensörün seçili AI modelinde tanıyabildiği
# nesnelerin tamamını aramasını sağlar.
#
# Hangi nesnelerin tanınacağı seçilen AI modeline bağlıdır.
# Örneğin V5RC Push Back modelinde mavi ve kırmızı bloklar,
# V5RC High Stakes modelinde ise mobile goal ve ring'ler
# bulunabilir.
# ------------------------------------------------------------

objects = ai_vision.take_snapshot(AiVision.ALL_AIOBJS)


# ------------------------------------------------------------
# 4. NESNE VAR MI?
# ------------------------------------------------------------
#
# take_snapshot() bir tuple döndürür.
#
# [0] en büyük algılanan nesneyi temsil eder.
#
# Önce exists kontrolü yapmak önemlidir. Hiç nesne yoksa
# doğrudan diğer özellikleri okumaya çalışmamalıyız.
# ------------------------------------------------------------

if objects[0].exists:
    brain.screen.print("Object detected")
else:
    brain.screen.print("No object detected")


# ------------------------------------------------------------
# 5. NESNENİN KONUMU
# ------------------------------------------------------------
#
# centerX ve centerY, algılanan nesnenin görüntü içindeki
# merkezini piksel cinsinden verir.
#
# AI Vision'ın görüntü çözünürlüğü 320 x 240 pikseldir.
# ------------------------------------------------------------

if objects[0].exists:

    x = objects[0].centerX
    y = objects[0].centerY

    brain.screen.print(x)
    brain.screen.print(y)


# ------------------------------------------------------------
# 6. NESNENİN BOYUTU
# ------------------------------------------------------------
#
# width ve height, algılanan nesnenin görüntüde kapladığı
# alanın genişlik ve yüksekliğini piksel cinsinden verir.
# ------------------------------------------------------------

if objects[0].exists:

    width = objects[0].width
    height = objects[0].height

    brain.screen.print(width)
    brain.screen.print(height)


# ------------------------------------------------------------
# 7. APRILTAG ALGILAMA
# ------------------------------------------------------------
#
# ALL_TAGS kullanarak kameranın gördüğü bütün AprilTag'leri
# arayabiliriz.
# ------------------------------------------------------------

tags = ai_vision.take_snapshot(AiVision.ALL_TAGS)


if tags[0].exists:
    brain.screen.print("AprilTag detected")


# ------------------------------------------------------------
# 8. OBJECT ID
# ------------------------------------------------------------
#
# id özelliği, algılanan AI nesnesinin veya AprilTag'in
# kimliğini verir.
#
# AI sınıflandırmalarında bu ID, kullanılan AI modeline göre
# değişir.
#
# Örneğin farklı nesneler farklı ID numaralarına sahip olabilir.
# ------------------------------------------------------------

if objects[0].exists:

    object_id = objects[0].id

    brain.screen.print(object_id)


# ------------------------------------------------------------
# 9. SCORE
# ------------------------------------------------------------
#
# score, AI sınıflandırmasının nesneyi tanıdığına ne kadar
# güvendiğini gösteren confidence score'dur.
#
# Bu özellik özellikle AI Classification sonuçlarında
# kullanışlıdır.
# ------------------------------------------------------------

if objects[0].exists:

    score = objects[0].score

    brain.screen.print(score)


# ------------------------------------------------------------
# 10. ANGLE
# ------------------------------------------------------------
#
# angle, algılanan Color Code veya AprilTag'in görüntü
# içindeki yönelimini derece cinsinden verir.
#
# Bu özellik AI Vision'ın her nesnesinde aynı şekilde
# kullanılmaz; özellikle yön bilgisi bulunan hedeflerde
# anlamlıdır.
# ------------------------------------------------------------

if tags[0].exists:

    tag_angle = tags[0].angle

    brain.screen.print(tag_angle)


# ------------------------------------------------------------
# 11. INSTALLED
# ------------------------------------------------------------
#
# installed(), AI Vision Sensor'ın Brain'e bağlı olup
# olmadığını kontrol eder.
# ------------------------------------------------------------

if ai_vision.installed():
    brain.screen.print("AI Vision connected")
else:
    brain.screen.print("AI Vision not connected")


# ------------------------------------------------------------
# 12. AI VISION İLE VISION SENSOR ARASINDAKİ FARK
# ------------------------------------------------------------
#
# Vision Sensor:
# Belirlediğimiz Color Signature ve Color Code'ları algılar.
#
# AI Vision Sensor:
# Bunlara ek olarak AI Classification ve AprilTag gibi
# daha gelişmiş görsel bilgileri de algılayabilir.
#
# Bu yüzden AI Vision, robotun görüntüyü daha anlamlı bir
# şekilde yorumlamasını sağlayabilir.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 13. AUTONOMOUS'TA KULLANIM
# ------------------------------------------------------------
#
# AI Vision ile örneğin belirli bir nesnenin görüntüdeki
# centerX değerini takip edebiliriz.
#
# Nesne görüntünün ortasından soldaysa robot sola,
# sağındaysa sağa dönmek gibi kararlar verebilir.
#
# Burada AI Vision yalnızca görüntüden veri sağlar.
# Hareket kararını ve motor kontrolünü program yapar.
# ------------------------------------------------------------


# ============================================================
# Ders 06 bitti, bir sonraki derse geçin.
# END OF 06 - AI VISION SENSOR
# ============================================================