# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 09 - COMPETITION
# ============================================================

from vex import *


# ============================================================
# 01 - COMPETITION NEDİR?
# ============================================================

# Competition sistemi, robotun yarışma sırasında
# Autonomous ve Driver Control bölümlerini yönetir.
#
# Temel yapı:
#
#     Autonomous
#          ↓
#     Driver Control
#
# Field Control System robotun hangi bölümde olduğunu
# belirler ve ilgili function çalıştırılır.


brain = Brain()


# ============================================================
# 02 - AUTONOMOUS FUNCTION
# ============================================================

def autonomous():

    brain.screen.clear_screen()
    brain.screen.print("AUTONOMOUS")

    # Autonomous kodu buraya yazılır.
    #
    # Örneğin ileride:
    #
    #     drive(...)
    #     turn(...)
    #     intake(...)
    #
    # gibi kendi function'larımızı çağıracağız.

    wait(15, SECONDS)


# ============================================================
# 03 - DRIVER CONTROL FUNCTION
# ============================================================

controller = Controller(PRIMARY)


def driver_control():

    brain.screen.clear_screen()
    brain.screen.print("DRIVER CONTROL")

    while True:

        # Controller kodları burada çalışır.
        #
        # Örneğin:
        #
        # left_speed = controller.axis3.position()
        # right_speed = controller.axis2.position()

        wait(20, MSEC)


# ============================================================
# 04 - COMPETITION OLUŞTURMA
# ============================================================

competition = Competition(
    driver_control,
    autonomous
)

# Python API'de Competition oluştururken iki function
# doğrudan constructor'a verilir:
#
#     Competition(driver_control, autonomous)
#
# İlk parameter:
#
#     driver_control
#
# Driver Control başladığında çalıştırılacak function'dır.
#
# İkinci parameter:
#
#     autonomous
#
# Autonomous başladığında çalıştırılacak function'dır.
#
# DİKKAT:
#
# Burada:
#
#     driver_control()
#
# veya:
#
#     autonomous()
#
# yazmıyoruz.
#
# Çünkü function'ı hemen çalıştırmak istemiyoruz.
# Competition sistemi gerektiğinde kendisi çağıracak.


# ============================================================
# 05 - PROGRAMIN ÇALIŞMAYA DEVAM ETMESİ
# ============================================================

while True:

    wait(100, MSEC)

# Competition callback'leri ayrı thread'ler olarak
# çalıştırılabildiği için ana programın da çalışmaya
# devam etmesi gerekir.
#
# Bu yüzden ana thread'i basit bir loop ile canlı tutuyoruz.
#
# Yarışma sırasında:
#
#             Competition
#                  |
#          +-------+-------+
#          |               |
#     Autonomous      Driver Control
#          |               |
#     autonomous()   driver_control()
#
# şeklinde çalışır.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Competition oluşturma:
#
#     competition = Competition(
#         driver_control,
#         autonomous
#     )
#
#
# Autonomous:
#
#     def autonomous():
#         ...
#
#
# Driver Control:
#
#     def driver_control():
#         ...
#
#
# ÖNEMLİ:
#
# Function'ın kendisini veriyoruz:
#
#     Competition(driver_control, autonomous)
#
# Function'ı çağırmıyoruz:
#
#     Competition(driver_control(), autonomous())
#
# YANLIŞ
#
#
# Autonomous ve Driver Control birbirinden ayrı
# function'lar olmalıdır.
#
# Autonomous içinde yarışmanın autonomous kısmına
# ait hareketler bulunur.
#
# Driver Control içinde ise sürücünün Controller
# üzerinden robotu kontrol ettiği loop bulunur.
#
#
# VEX Python'da Competition yapısı:
#
#     from vex import *
#
#     brain = Brain()
#
#     def autonomous():
#         ...
#
#     def driver_control():
#         ...
#
#     competition = Competition(
#         driver_control,
#         autonomous
#     )
#
#     while True:
#         wait(100, MSEC)
#
#
# Bu yapı ileride oluşturacağımız gerçek yarışma
# programının temelini oluşturacak.


# ============================================================
# Ders 09 bitti, sıradaki derse geçin.
# END OF 09 - COMPETITION
# ============================================================