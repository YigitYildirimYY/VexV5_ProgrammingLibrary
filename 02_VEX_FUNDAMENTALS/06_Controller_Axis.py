# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 02_VEX_FUNDAMENTALS
# Yiğit YILDIRIM
# 06 - CONTROLLER AXIS
# ============================================================

from vex import *


# ============================================================
# 01 - AXIS NEDİR?
# ============================================================

brain = Brain()
controller = Controller(PRIMARY)

# Controller üzerindeki joystickler AXIS olarak okunur.
#
# Her axis bir sayı döndürür.
#
# Genel aralık:
#
#     -100
#       0
#     +100
#
# 0:
#     Joystick merkezde.
#
# Pozitif / negatif:
#     Joystick'in hangi yöne hareket ettiğini gösterir.
#
# VEX Controller'da dört temel axis vardır:
#
#     axis1
#     axis2
#     axis3
#     axis4


# ============================================================
# 02 - AXIS DEĞERİNİ OKUMA
# ============================================================

value = controller.axis3.position()

brain.screen.clear_screen()
brain.screen.print(f"Axis 3: {value}")

# position() joystick'in o anki konumunu verir.
#
# Örneğin:
#
#     value = controller.axis3.position()
#
# value artık bir integer'dır.
#
# Bunu motor hızına doğrudan aktarabiliriz:
#
#     motor.spin(FORWARD, value, PERCENT)
#
# Bu, driver control kodunun temelini oluşturur.


# ============================================================
# 03 - AXIS İLE MOTOR KONTROLÜ
# ============================================================

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

# Bu yapı Tank Drive'ın temelidir.
#
# axis3 → sol taraf
# axis2 → sağ taraf
#
# Joystick ne kadar hareket ettirilirse motorun
# hızı da o kadar değişir.
#
# Joystick merkezdeyse:
#
#     position() ≈ 0
#
# dolayısıyla motor hızı da 0 olur.


# ============================================================
# 04 - DEADZONE
# ============================================================

# Joystick fiziksel olarak tam merkezde olsa bile
# küçük değerler okuyabilir.
#
# Örneğin:
#
#     0
#     1
#     -2
#     3
#
# gibi küçük değerler robotun istemeden hareket
# etmesine neden olabilir.
#
# Bunun için DEADZONE kullanılır.

def apply_deadzone(value, deadzone):

    if abs(value) < deadzone:

        return 0

    return value


left_speed = controller.axis3.position()
right_speed = controller.axis2.position()

left_speed = apply_deadzone(left_speed, 5)
right_speed = apply_deadzone(right_speed, 5)

# Burada:
#
#     abs(value)
#
# değerin mutlak değerini verir.
#
# Örneğin:
#
#     abs(-4) = 4
#
# Eğer joystick değeri ±5 aralığındaysa
# 0 kabul ediyoruz.
#
# Bu yöntem driver control'de çok önemlidir.


# ============================================================
# 05 - AXIS DEĞERİNİ DÖNÜŞTÜRME
# ============================================================

# Joystick değerini doğrudan kullanmak zorunda değiliz.
#
# Örneğin robotun daha yumuşak hareket etmesini
# istiyorsak değeri değiştirebiliriz.

def curve_input(value):

    return (value * abs(value)) / 100


value = controller.axis3.position()

speed = curve_input(value)
"""
 Normalde:

     joystick → motor

 şeklinde doğrudan aktarım yapıyoruz.

 Curve kullanırsak:

     joystick
         ↓
     input curve
         ↓
     motor

 olur.

 Bu özellikle küçük joystick hareketlerinde robotun
 daha hassas kontrol edilmesini sağlayabilir.

 Ancak burada dikkat:

 Driver control için kullanılacak input curve,
 robotun mekanik yapısına ve sürücünün tercihine göre
 ayarlanmalıdır.
"""

# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Axis okuma:
#
#     controller.axis1.position()
#     controller.axis2.position()
#     controller.axis3.position()
#     controller.axis4.position()
#
# position():
#     Joystick'in mevcut değerini verir.
#
# Genel aralık:
#
#     -100 → 0 → +100
#
#
# En temel driver control:
#
#     speed = controller.axis3.position()
#
#     motor.spin(
#         FORWARD,
#         speed,
#         PERCENT
#     )
#
#
# Deadzone:
#
#     Küçük joystick değerlerini 0 yapmak.
#
#
# Input Curve:
#
#     Joystick değerini daha hassas veya daha agresif
#     bir kontrol için dönüştürmek.
#
#
# En önemli mantık:
#
# Controller Axis
#        ↓
#   Sayısal değer
#        ↓
#  İşleme / filtreleme
#        ↓
#      Motor
#
# Bu yapı ileride:
#
#     Tank Drive
#     Arcade Drive
#     Curvature Drive
#
# sistemlerinin temelini oluşturacak.



# ============================================================
# Ders 06 bitti, sıradaki derse geçin.
# END OF 06 - CONTROLLER AXIS
# ============================================================