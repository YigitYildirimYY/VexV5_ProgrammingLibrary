# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 01 - VEX BRAIN
# ============================================================

# VEX Python programlarında Brain, robotun ana bilgisayarıdır.
#
# Motorlar, sensörler ve Controller gibi cihazlarla
# çalışırken Brain programın merkezindeki cihazdır.
#
# İlk olarak VEX kütüphanesini import ederiz.

from vex import *


# ============================================================
# 01 - BRAIN OLUŞTURMA
# ============================================================

brain = Brain()

# Brain() yeni bir Brain nesnesi oluşturur.
#
# Bundan sonra Brain'in özelliklerine:
#
#     brain
#
# üzerinden ulaşabiliriz.
#
# Örneğin Brain'in ekranına yazı yazmak için:
#
#     brain.screen.print("Hello")
#
# kullanabiliriz.


# ============================================================
# 02 - BRAIN EKRANI
# ============================================================

brain.screen.clear_screen()

brain.screen.print("Hello VEX")

# brain.screen, Brain'in üzerindeki dokunmatik ekranı
# kontrol eder.
#
# clear_screen():
#     Ekranı temizler.
#
# print():
#     Ekrana yazı yazdırır.
#
# Örneğin:

brain.screen.clear_screen()

brain.screen.print("Robot Ready")

# Bu yapı robot açıldığında ekrana bilgi vermek için
# oldukça kullanışlıdır.


# ============================================================
# 03 - EKRANA FARKLI VERİLER YAZDIRMA
# ============================================================

speed = 80

brain.screen.print("Speed: ")
brain.screen.print(speed)

# Python'daki variable'ları da ekrana yazdırabiliriz.
#
# Daha düzenli bir kullanım için formatlama da yapılabilir:

brain.screen.clear_screen()

brain.screen.print("Speed: %d%%" % speed)

# Buradaki %d integer değeri yazdırır.
#
# Ancak Python'da daha modern bir yöntem de vardır:

brain.screen.clear_screen()

brain.screen.print(f"Speed: {speed}%")

# f-string kullanımı özellikle debug ekranlarında
# oldukça kullanışlıdır.


# ============================================================
# 04 - BRAIN İLE TEMEL ZAMANLAMA
# ============================================================

brain.screen.clear_screen()

brain.screen.print("Starting...")

wait(2, SECONDS)

brain.screen.clear_screen()

brain.screen.print("2 seconds passed")

# wait(), programın belirli bir süre beklemesini sağlar.
#
# Kullanımı:
#
#     wait(süre, birim)
#
# Örneğin:
#
#     wait(1, SECONDS)
#     wait(500, MSEC)
#
# Burada wait() doğrudan Brain'in bir method'u değildir.
# VEX Python API'sinin zamanlama fonksiyonlarından biridir.


# ============================================================
# 05 - BRAIN'İN VEX PROGRAMINDAKİ ROLÜ
# ============================================================

# Basit bir VEX programının genel yapısı şöyle olabilir:

from vex import *

brain = Brain()

brain.screen.clear_screen()
brain.screen.print("Robot Ready")

wait(2, SECONDS)

brain.screen.clear_screen()
brain.screen.print("Program Started")

# Burada henüz motor veya sensör kullanmadık.
#
# Ancak temel yapı kurulmuş oldu:
#
#     from vex import *
#             |
#             v
#        Brain oluştur
#             |
#             v
#       Brain üzerinden
#       ekran vb. kullan
#             |
#             v
#       Robot programını çalıştır
#
# İlerleyen dosyalarda Brain'in yanında:
#
#     Motor
#     Controller
#     Sensors
#     Competition
#
# gibi cihazları ekleyeceğiz.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# from vex import *
#     VEX Python API'sini programa dahil eder.
#
# brain = Brain()
#     Brain nesnesi oluşturur.
#
# brain.screen
#     Brain ekranına erişir.
#
# brain.screen.clear_screen()
#     Ekranı temizler.
#
# brain.screen.print(...)
#     Ekrana veri yazdırır.
#
# wait(...)
#     Programı belirli süre bekletir.
#
# Brain'i robotun "beyni" olarak düşünebilirsin.
# Diğer VEX cihazları ileride bu temel yapı üzerine
# bağlanacak.



# ============================================================
# Ders 01 bitti, sıradaki derse geçebilirsiniz.
# END OF 01 - VEX BRAIN
# ============================================================