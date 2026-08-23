# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 04 - CONTROLLER
# ============================================================

from vex import *


# ============================================================
# 01 - CONTROLLER NEDİR?
# ============================================================

# Controller, sürücünün robotu kontrol etmesini sağlayan
# VEX kumandasıdır.
#
# Python'da Controller() ile bir Controller device'ı
# oluştururuz.
#
# Genellikle Controller'ı programın başında oluştururuz.

brain = Brain()

controller = Controller(PRIMARY)

# PRIMARY:
#     Ana Controller'ı belirtir.
#
# Controller oluşturulduktan sonra:
#
#     controller
#
# üzerinden joystick, buton ve Controller ekranı gibi
# özelliklere erişebiliriz.


# ============================================================
# 02 - CONTROLLER AXIS
# ============================================================

controller = Controller(PRIMARY)

left_axis = controller.axis3.position()
right_axis = controller.axis2.position()

print(left_axis)
print(right_axis)

# Joystick eksenlerinden değer almak için:
#
#     axis1
#     axis2
#     axis3
#     axis4
#
# kullanılır.
#
# position() joystick'in mevcut konumunu döndürür.
#
# Değer genellikle:
#
#     -100 → bir yön
#       0  → merkez
#     +100 → diğer yön
#
# aralığındadır.
#
# Hangi axis'in hangi joystick hareketine karşılık
# geldiğini Controller'ın fiziksel düzenine göre
# öğrenmek önemlidir.


# ============================================================
# 03 - CONTROLLER BUTTON
# ============================================================

controller = Controller(PRIMARY)

if controller.buttonA.pressing():

    print("A button pressed")

# Bir butonun basılı olup olmadığını:
#
#     pressing()
#
# ile kontrol edebiliriz.
#
# Örneğin:
#
#     buttonA
#     buttonB
#     buttonX
#     buttonY
#
# gibi butonlara erişebiliriz.
#
# Diğer Controller butonlarını da aynı mantıkla
# kullanabiliriz.
#
# Burada önemli nokta:
#
#     pressing()
#
# bir boolean değer döndürür:
#
#     True
#     False


# ============================================================
# 04 - CONTROLLER EKRANI VE RUMBLE
# ============================================================

controller = Controller(PRIMARY)

controller.screen.clear_screen()

controller.screen.set_cursor(1, 1)

controller.screen.print("Robot Ready")

# Controller'ın kendi ekranı da vardır.
#
# screen.clear_screen():
#     Ekranı temizler.
#
# screen.set_cursor(row, column):
#     Yazının başlayacağı konumu belirler.
#
# screen.print():
#     Ekrana yazı yazdırır.
#
# Controller ayrıca titreşim verebilir:

controller.rumble(".")

# Rumble(), sürücüye kısa bir titreşim gönderir.
#
# Bu örneğin:
#
#     belirli bir olay gerçekleşti
#     uyarı ver
#     robot hazır
#
# gibi durumlarda kullanılması mümkündür.


# ============================================================
# 05 - DRIVER CONTROL TEMELİ
# ============================================================

brain = Brain()

controller = Controller(PRIMARY)

left_motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

right_motor = Motor(
    Ports.PORT2,
    GearSetting.RATIO_18_1,
    True
)

while True:

    left_speed = controller.axis3.position()
    right_speed = controller.axis2.position()

    left_motor.spin(
        FORWARD,
        left_speed,
        PERCENT
    )

    right_motor.spin(
        FORWARD,
        right_speed,
        PERCENT
    )

    wait(20, MSEC)

# Burada Controller ile motorları birbirine bağladık.
#
# axis3:
#     Sol motorun hızını kontrol ediyor.
#
# axis2:
#     Sağ motorun hızını kontrol ediyor.
#
# position():
#     Joystick değerini alıyor.
#
# motor.spin():
#     Motoru bu değerde çalıştırıyor.
#
# while True:
#     Driver Control devam ettiği sürece sistemi
#     sürekli güncelliyor.
#
# wait(20, MSEC):
#     Loop'un aşırı hızlı çalışmasını önlüyor.
#
# Bu, ileride yazacağımız Tank Drive'ın en temel
# halidir.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Controller:
#
#     controller = Controller(PRIMARY)
#
# Controller Axis:
#
#     controller.axis3.position()
#
# Controller Button:
#
#     controller.buttonA.pressing()
#
# Controller Screen:
#
#     controller.screen.print(...)
#
# Controller Rumble:
#
#     controller.rumble(".")
#
# En önemli mantık:
#
#     Controller
#          ↓
#     Input değerleri
#          ↓
#     Robot kontrolü
#
# Controller'ın kendisi robotu hareket ettirmez.
# Controller'dan aldığımız input değerlerini motor,
# piston veya diğer sistemlere gönderen kodu biz yazarız.
#
# İlerleyen dosyalarda Controller'ı:
#
#     Buttons
#     Axis
#     Deadzone
#     Driver Control
#
# ile çok daha ayrıntılı şekilde kullanacağız.


# ============================================================
# Ders 04 bitti, sıradaki derse geçin.
# END OF 04 - CONTROLLER
# ============================================================