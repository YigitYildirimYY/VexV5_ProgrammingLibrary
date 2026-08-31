# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 10 - THREADS
# ============================================================

#NOTE#
#Thread komutunun kullanımı opsiyoneldir ve robotunuzun asıl kodunu karmaşıklaştıracaktır, 33900A takımı olarak kodumuzda bu yüzden thread komutunu kullanmamaktayız (17.07.2026)

from vex import *


brain = Brain()


# ============================================================
# 01 - THREAD NEDİR?
# ============================================================
# Normal bir Python programında kod genellikle sırayla
# çalışır.
#
# Örneğin:
#
#     motor.spin()
#     wait(...)
#     screen.print(...)
#
# İlk işlem tamamlanmadan ikinci işlem başlamaz.
#
# Thread ise bir function'ın programın geri kalanından
# bağımsız şekilde çalışmasına izin verir.
#
# Robotlarda bu çok önemlidir.
#
# Örneğin aynı anda:
#
#     Motorları kontrol et
#     Sensörleri oku
#     Ekranı güncelle
#
# isteyebiliriz.


# ============================================================
# 02 - THREAD OLUŞTURMA
# ============================================================

def display_status():

    while True:

        brain.screen.clear_screen()
        brain.screen.print("Robot Running")

        wait(500, MSEC)


status_thread = Thread(display_status)

# Thread() içine function'ın kendisini veririz.
#
# DOĞRU:
#
#     Thread(display_status)
#
# YANLIŞ:
#
#     Thread(display_status())
#
# Çünkü display_status() yazarsak function'ı hemen
# çalıştırmış oluruz.
#
# Thread(display_status) ise:
#
#     "Bu function'ı ayrı bir thread'de çalıştır."
#
# anlamına gelir.
#
# Thread oluşturulduğu anda function çalışmaya başlar.


# ============================================================
# 03 - AYNI ANDA BİRDEN FAZLA İŞLEM
# ============================================================
"""
def update_screen():

    while True:

        brain.screen.clear_screen()
        brain.screen.print("Screen Thread")

        wait(100, MSEC)


def background_task():

    while True:

        # Burada robotun arka planda yapmasını istediğimiz
        # başka bir işlem bulunabilir.

        wait(100, MSEC)


screen_thread = Thread(update_screen)
background_thread = Thread(background_task)
"""

# Artık iki function ayrı thread'lerde çalışabilir:
#
#     update_screen()
#            +
#     background_task()
#
# Bu, robot yazılımında multitasking mantığının
# temelidir.
#
# Örneğin ileride:
#
#     Sensor monitoring
#     Odometry update
#     Debug screen
#
# gibi işlemleri ayrı thread'lerde çalıştırabiliriz.


# ============================================================
# 04 - THREAD'İ DURDURMA
# ============================================================

def background_task():

    while True:

        brain.screen.print("Running")

        wait(100, MSEC)


task_thread = Thread(background_task)

wait(2, SECONDS)

task_thread.stop()

# stop() ilgili thread'i durdurur.
#
# Örneğin:
#
#     task_thread.stop()
#
# dediğimizde background_task thread'i durur.
#
# ÖNEMLİ:
#
# VEX API'ye göre durdurulan bir Thread tekrar
# başlatılamaz.
#
# Yeniden çalıştırmak istiyorsak yeni bir Thread
# oluşturmamız gerekir:
#
#     task_thread = Thread(background_task)


# ============================================================
# 05 - THREAD KULLANIRKEN DİKKAT
# ============================================================

# Thread güçlü bir araçtır ancak her şeyi thread'e
# ayırmak doğru değildir.
#
# Özellikle iki farklı thread'in aynı motoru kontrol
# etmesi sorun oluşturabilir.
#
# Örneğin:
#
# Thread 1:
#
#     left_motor.spin(FORWARD, 50, PERCENT)
#
# Thread 2:
#
#     left_motor.spin(REVERSE, 100, PERCENT)
#
# gibi bir durumda iki farklı kod aynı cihazı kontrol
# etmeye çalışır.
#
# Bu nedenle robot mimarisinde:
#
#     Bir cihazın kontrolünden hangi function/thread
#     sorumlu?
#
# sorusunu baştan belirlemek önemlidir.
#
# Ayrıca sonsuz loop kullanan thread'lerde küçük bir
# wait() bulunması iyi bir uygulamadır:
#
#     while True:
#
#         ...
#
#         wait(20, MSEC)
#
# Böylece thread sürekli gereksiz şekilde dönmez.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Function:
#
#     def task():
#         ...
#
#
# Thread oluşturma:
#
#     my_thread = Thread(task)
#
#
# Thread durdurma:
#
#     my_thread.stop()
#
#
# DOĞRU:
#
#     Thread(task)
#
#
# YANLIŞ:
#
#     Thread(task())
#
#
# Thread'in temel amacı:
#
#     Birden fazla bağımsız işlemi aynı program içinde
#     eş zamanlı yürütmektir.
#
#
# VEX'te kullanım alanları:
#
#     Sensor monitoring
#     Odometry
#     Debug screen
#     Background calculations
#     Autonomous yardımcı işlemleri
#
#
# En önemli kural:
#
# Aynı motoru veya mekanizmayı birden fazla thread'in
# kontrol etmesine mümkün olduğunca izin verme.
#
# Thread'leri robot mimarisinde kontrollü kullan.





# ============================================================
# Ders 10 bitti, sıradaki derse geçin.
# END OF 10 - THREADS
# ============================================================


"""
BU DERSLE BERABER VEX_FUNDAMENTALS KONUSU BITTI.

Sıradaki konu;
MOTORS
"""
