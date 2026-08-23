# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 08 - WAIT
# ============================================================

from vex import *


brain = Brain()


# ============================================================
# 01 - WAIT NEDİR?
# ============================================================

# wait(), programın belirli bir süre duraklamasını sağlar.
#
# Temel kullanım:
#
#     wait(süre, birim)
#
# Örneğin:

wait(1, SECONDS)

# Program burada 1 saniye bekler ve ardından devam eder.
#
# wait() özellikle robotun belirli bir sırayla hareket
# etmesini istediğimiz durumlarda çok kullanılır.


# ============================================================
# 02 - ZAMAN BİRİMLERİ
# ============================================================

wait(1, SECONDS)

wait(500, MSEC)

# En sık kullanacağımız birimler:
#
#     SECONDS
#     MSEC
#
# Örnek:
#
#     wait(2, SECONDS)
#
# 2 saniye bekler.
#
#     wait(200, MSEC)
#
# 200 milisaniye = 0.2 saniye bekler.
#
# Dönüşüm:
#
#     1 SECOND = 1000 MSEC


# ============================================================
# 03 - MOTOR HAREKETİNDE WAIT
# ============================================================

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

motor.set_velocity(50, PERCENT)

motor.spin(FORWARD)

wait(2, SECONDS)

motor.stop()

# Burada işlem sırası şöyledir:
#
#     Motor çalıştır
#          ↓
#     2 saniye bekle
#          ↓
#     Motoru durdur
#
# Yani wait() sadece "programı durdurmak" için değil,
# robot hareketlerini zamanlamak için de kullanılabilir.


# ============================================================
# 04 - LOOP İÇİNDE WAIT
# ============================================================

controller = Controller(PRIMARY)

while True:

    speed = controller.axis3.position()

    motor.spin(
        FORWARD,
        speed,
        PERCENT
    )

    wait(20, MSEC)

# Burada wait() çok daha önemli bir görev üstleniyor.
#
# Loop'un:
#
#     mümkün olduğunca kontrollü
#     ve düzenli
#
# şekilde tekrar çalışmasını sağlıyor.
#
# wait() olmadan loop gereksiz şekilde çok hızlı
# çalışabilir ve işlemciyi gereksiz yere meşgul edebilir.
#
# Driver Control kodlarında küçük bir wait kullanmak
# yaygın bir uygulamadır.


# ============================================================
# 05 - WAIT VE TIMER ARASINDAKİ FARK
# ============================================================

# wait():

wait(1, SECONDS)

# "1 saniye BEKLE."
#
#
# Timer:

elapsed = brain.timer.time(SECONDS)

# "Ne kadar ZAMAN GEÇTİ?"
#
# Bunlar aynı şey değildir.
#
# wait() zamanı geçirmek için kullanılır.
#
# timer zamanı ölçmek için kullanılır.
#
# Örneğin autonomous'ta:
#
#     wait(1, SECONDS)
#
# belirli bir hareketi zamanlamak için kullanılabilir.
#
# Buna karşılık:
#
#     start = brain.timer.time(MSEC)
#
#     ...
#
#     elapsed = brain.timer.time(MSEC) - start
#
# ile bir hareketin gerçekten ne kadar sürdüğünü
# ölçebiliriz.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Temel kullanım:
#
#     wait(1, SECONDS)
#
#     wait(500, MSEC)
#
#
# En önemli birimler:
#
#     SECONDS
#     MSEC
#
#
# wait():
#     Programın belirli süre beklemesini sağlar.
#
#
# Timer:
#     Geçen süreyi ölçer.
#
#
# Önemli VEX kullanım alanları:
#
#     Autonomous
#     Motor hareketleri
#     Driver Control loop'ları
#     Sensor polling
#     State machines
#
#
# Özellikle loop'larda:
#
#     while True:
#
#         ...
#
#         wait(20, MSEC)
#
# gibi küçük bir bekleme kullanmak önemlidir.
#
# Ancak wait() değerini gereksiz yere çok büyük yapmak
# robotun kontrolünün yavaşlamasına neden olabilir.



# ============================================================
# Ders 08 bitti, bir sonraki derse geçin.
# END OF 08 - WAIT
# ============================================================