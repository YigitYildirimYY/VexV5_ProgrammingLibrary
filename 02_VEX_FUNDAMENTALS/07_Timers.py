# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 07 - TIMERS
# ============================================================

from vex import *


brain = Brain()


# ============================================================
# 01 - TIMER NEDİR?
# ============================================================

# Robot programlarında zamanı ölçmek çok önemlidir.
#
# Örneğin:
#
#     "Motor 2 saniye çalışsın."
#     "Autonomous 15 saniye sürüyor mu?"
#     "Bir hareket ne kadar sürdü?"
#
# gibi durumlarda timer kullanabiliriz.
#
# VEX'te Brain'in timer özelliğini kullanabiliriz.


# ============================================================
# 02 - BRAIN TIMER
# ============================================================

time = brain.timer.time(SECONDS)

print(time)

# brain.timer.time() programın ne kadar süredir
# çalıştığını ölçmek için kullanılır.
#
# Birim belirtebiliriz:
#
#     SECONDS
#     MSEC
#
# Örneğin:

seconds = brain.timer.time(SECONDS)

milliseconds = brain.timer.time(MSEC)

print(seconds)
print(milliseconds)

# SECONDS:
#     Saniye cinsinden zaman.
#
# MSEC:
#     Milisaniye cinsinden zaman.
#
# 1 saniye = 1000 milisaniye


# ============================================================
# 03 - TIMER İLE GEÇEN ZAMANI ÖLÇME
# ============================================================

start_time = brain.timer.time(MSEC)

wait(500, MSEC)

end_time = brain.timer.time(MSEC)

elapsed_time = end_time - start_time

print(elapsed_time)

# Burada önemli bir yöntem kullanıyoruz:
#
#     başlangıç zamanı
#            ↓
#     işlem gerçekleşiyor
#            ↓
#     bitiş zamanı
#
# Sonra:
#
#     elapsed = end - start
#
# ile işlemin ne kadar sürdüğünü buluyoruz.
#
# Bu yöntem özellikle robot hareketlerinin performansını
# ölçerken çok kullanışlıdır.


# ============================================================
# 04 - TIMER İLE KOŞUL OLUŞTURMA
# ============================================================

start_time = brain.timer.time(SECONDS)

while True:

    elapsed = brain.timer.time(SECONDS) - start_time

    if elapsed >= 3:

        break

    brain.screen.clear_screen()
    brain.screen.print(f"Time: {elapsed}")

    wait(20, MSEC)

# Burada program:
#
#     3 saniye geçene kadar
#
# loop içinde kalıyor.
#
# 3 saniyeye ulaşıldığında:
#
#     break
#
# ile loop'tan çıkıyoruz.
#
# Bu yöntem özellikle autonomous'ta zaman sınırlı
# hareketler oluşturmak için kullanılabilir.


# ============================================================
# 05 - TIMER'I RESETLEME
# ============================================================

brain.timer.clear()

# clear() timer değerini sıfırlar.
#
# Bundan sonra:
#
#     brain.timer.time(...)
#
# yeniden 0'dan itibaren zaman ölçmeye başlar.
#
# Örneğin bir autonomous hareketinden önce:

brain.timer.clear()

# ardından:

start_time = brain.timer.time(MSEC)

# kullanarak o hareketin süresini ayrı şekilde
# ölçebiliriz.
#
# NOT:
# Timer'ı sürekli resetlemek yerine çoğu zaman
# başlangıç zamanını bir variable'da saklamak daha
# kontrollü bir yöntemdir.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Zaman ölçme:
#
#     brain.timer.time(SECONDS)
#
# veya:
#
#     brain.timer.time(MSEC)
#
#
# Geçen zamanı bulma:
#
#     start = brain.timer.time(MSEC)
#
#     ...
#
#     end = brain.timer.time(MSEC)
#
#     elapsed = end - start
#
#
# Timer sıfırlama:
#
#     brain.timer.clear()
#
#
# En önemli ayrım:
#
# wait()
#     Programı bekletir.
#
# timer
#     Zamanı ölçer.
#
# Örneğin:
#
#     wait(2, SECONDS)
#
# "2 saniye bekle" demektir.
#
# Buna karşılık:
#
#     brain.timer.time(SECONDS)
#
# "Şu ana kadar ne kadar zaman geçti?" demektir.
#
#
# VEX'te timer özellikle:
#
#     Autonomous
#     Debugging
#     Performance measurement
#     Time limits
#     State machines
#
# gibi sistemlerde çok önemlidir.




# ============================================================
# Ders 07 bitti, sıradaki derse geçin.
# END OF 07 - TIMERS
# ============================================================