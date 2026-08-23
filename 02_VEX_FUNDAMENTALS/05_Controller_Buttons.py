# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 05 - CONTROLLER BUTTONS
# ============================================================

from vex import *


# ============================================================
# 01 - BUTONLARA ERİŞME
# ============================================================

brain = Brain()
controller = Controller(PRIMARY)

# Controller üzerindeki butonlara doğrudan
# controller nesnesi üzerinden erişebiliriz.
#
# Örnek:
#
#     controller.buttonA
#     controller.buttonB
#     controller.buttonX
#     controller.buttonY
#
# Diğer butonlar da aynı mantıkla kullanılabilir.


# ============================================================
# 02 - PRESSING()
# ============================================================

if controller.buttonA.pressing():

    brain.screen.print("A is pressed")

# pressing() butonun o anda basılı olup olmadığını
# kontrol eder.
#
# Sonuç:
#
#     True
#     False
#
# Örneğin:
#
#     if controller.buttonA.pressing():
#
# A basılıysa if bloğu çalışır.


# ============================================================
# 03 - BUTON İLE MOTOR KONTROLÜ
# ============================================================

motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)

while True:

    if controller.buttonA.pressing():

        motor.spin(FORWARD, 50, PERCENT)

    else:

        motor.stop()

    wait(20, MSEC)

# Burada A basılı tutulduğu sürece motor çalışır.
#
# A bırakıldığında:
#
#     else
#         ↓
#     motor.stop()
#
# çalışır.
#
# Bu yapı özellikle intake, clamp veya mekanizma
# kontrolünde çok kullanılır.


# ============================================================
# 04 - BİR BUTONLA AÇ/KAPA MANTIĞI
# ============================================================

# Bazen butona basılı tuttuğumuz sürece değil,
# butona her basıldığında bir işlemi değiştirmek isteriz.
#
# Örneğin:
#
#     A'ya bas → intake aç
#     A'ya tekrar bas → intake kapat
#
# Bunun için sadece pressing() kullanmak yeterli değildir.
#
# Bir önceki buton durumunu saklamamız gerekir.

intake_on = False
previous_a = False

while True:

    current_a = controller.buttonA.pressing()

    if current_a and not previous_a:

        intake_on = not intake_on

    previous_a = current_a

    if intake_on:

        motor.spin(FORWARD, 100, PERCENT)

    else:

        motor.stop()

    wait(20, MSEC)

# Buradaki önemli fikir:
#
# current_a:
#     Şu anki buton durumu.
#
# previous_a:
#     Önceki loop'taki buton durumu.
#
# Eğer:
#
#     current_a == True
#     previous_a == False
#
# ise butona yeni basılmış demektir.
#
# Böylece tek bir basışı bir kez algılayabiliriz.


# ============================================================
# 05 - BUTTON EVENT MANTIĞI
# ============================================================

# VEX Controller button'larında ayrıca event tabanlı
# callback mantığı da kullanılabilir.
#
# Örneğin bir butona basıldığında belirli bir
# function çalıştırabiliriz.

def button_pressed():

    brain.screen.print("Button pressed")


controller.buttonA.pressed(button_pressed)

# Burada:
#
# button_pressed()
#
# function'ını doğrudan çalıştırmıyoruz.
#
# Onu VEX'e callback olarak veriyoruz:
#
#     pressed(button_pressed)
#
# A butonuna basıldığında VEX bu function'ı çağırır.
#
# Bu yaklaşım büyük programlarda bazı olayları
# temiz şekilde ayırmak için kullanılabilir.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Butona erişim:
#
#     controller.buttonA
#
# Basılı mı?
#
#     controller.buttonA.pressing()
#
# Sonuç:
#
#     True / False
#
#
# Basılı tutulduğu sürece işlem:
#
#     if controller.buttonA.pressing():
#
#         ...
#
#
# Tek basışı algılama:
#
#     current_a
#     previous_a
#
# mantığı kullanılır.
#
#
# Event/callback:
#
#     controller.buttonA.pressed(function)
#
#
# En önemli ayrım:
#
# pressing()
#     Butonun şu anki durumunu sürekli kontrol eder.
#
# pressed()
#     Butona basılma olayında bir function çağırabilir.
#
# Driver Control'de butonları genellikle:
#
#     Intake
#     Clamp
#     Pneumatics
#     Lift
#     Endgame mechanisms
#
# gibi sistemleri kontrol etmek için kullanacağız.



# ============================================================
# Ders 05 bitti, sıradaki derse geçin.
# END OF 05 - CONTROLLER BUTTONS
# ============================================================