# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 04 - SENSORS
# Yiğit YILDIRIM
# 04 - OPTICAL SENSOR
# ============================================================


from vex import *


# ------------------------------------------------------------
# 1. OPTICAL SENSOR NEDİR?
# ------------------------------------------------------------
#
# Optical Sensor; renk, parlaklık ve yakındaki nesnelerin
# varlığı hakkında bilgi verir.
#
# Sensör RGB renk sensörü ve proximity sensörü kullanır.
# Ayrıca kendi LED ışığı vardır.
#
# En sık kullanım alanları:
# - Nesne rengini algılamak
# - Nesne olup olmadığını anlamak
# - Yüzeyin parlaklığını ölçmek
# - Belirli renkleri ayırt etmek
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. SENSOR TANIMLAMA
# ------------------------------------------------------------

brain = Brain()

optical = Optical(Ports.PORT7)


# ------------------------------------------------------------
# 3. SENSOR LED'İ
# ------------------------------------------------------------
#
# Optical Sensor'ın kendi LED ışığını açabilir veya
# kapatabiliriz.
#
# Renk algılarken LED kullanmak ölçümlerin daha tutarlı
# olmasına yardımcı olabilir.
# ------------------------------------------------------------

optical.set_light(LedStateType.ON)


# LED'in parlaklığını da yüzde olarak ayarlayabiliriz.

optical.set_light_power(50, PERCENT)


# ------------------------------------------------------------
# 4. YAKINDA NESNE VAR MI?
# ------------------------------------------------------------
#
# is_near_object() sensörün çalışma alanında bir nesne
# algılayıp algılamadığını True veya False olarak verir.
# ------------------------------------------------------------

if optical.is_near_object():
    brain.screen.print("Object detected")
else:
    brain.screen.print("No object")


# ------------------------------------------------------------
# 5. RENK ALGILAMA
# ------------------------------------------------------------
#
# color() algılanan renge karşılık gelen bir Color nesnesi
# döndürür.
#
# Hazır renklerden bazıları:
#
# Color.RED
# Color.BLUE
# Color.GREEN
# Color.YELLOW
# Color.ORANGE
# Color.PURPLE
# Color.CYAN
# Color.BLACK
# Color.WHITE
# ------------------------------------------------------------

if optical.color() == Color.RED:
    brain.screen.print("Red")

elif optical.color() == Color.BLUE:
    brain.screen.print("Blue")


# ------------------------------------------------------------
# 6. BRIGHTNESS
# ------------------------------------------------------------
#
# brightness(), nesneden sensöre geri yansıyan ışık miktarını
# yüzdeyi temsil eden bir float olarak verir.
#
# Daha yüksek değer, sensöre daha fazla ışık yansıdığı
# anlamına gelir.
# ------------------------------------------------------------

brightness = optical.brightness()

brain.screen.print(brightness)


# ------------------------------------------------------------
# 7. HUE
# ------------------------------------------------------------
#
# hue(), algılanan rengin hue değerini 0 ile 359 arasında
# bir float olarak verir.
#
# color() hazır renkleri kontrol etmek için daha kolaydır.
# hue() ise belirli bir renk aralığını kendimiz seçmemize
# izin verir.
# ------------------------------------------------------------

hue = optical.hue()

brain.screen.print(hue)


# Örneğin belirli bir hue aralığını kontrol edebiliriz.

if 300 < optical.hue() < 359:
    brain.screen.print("Hue detected")


# ------------------------------------------------------------
# 8. RENK VE HUE ARASINDAKİ FARK
# ------------------------------------------------------------
#
# color() bize VEX'in tanımladığı renklerden birini verir.
#
# Örneğin:
#
#     optical.color() == Color.RED
#
# hue() ise doğrudan sayısal değer verir.
#
# Bu yüzden kendi renk aralıklarımızı oluşturmak istediğimizde
# hue() daha kullanışlıdır.
#
# Örneğin resmi VEX dokümanında 300° - 359° aralığı bir
# pembe tonunu algılamak için örnek olarak kullanılmıştır.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 9. PRATİK KULLANIM
# ------------------------------------------------------------
#
# Sensörü sürekli okuyarak önünde kırmızı veya mavi bir
# nesne olup olmadığını kontrol edebiliriz.
# ------------------------------------------------------------

while True:

    if optical.is_near_object():

        if optical.color() == Color.RED:
            brain.screen.print("Red detected")

        elif optical.color() == Color.BLUE:
            brain.screen.print("Blue detected")

    wait(20, MSEC)


# ============================================================
# Ders 04 bitti, bir sonraki derse geçin.
# END OF 04 - OPTICAL SENSOR
# ============================================================