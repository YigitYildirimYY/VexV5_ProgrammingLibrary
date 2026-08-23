# ============================================================
# 33900A VEX V5 PYTHON PROGRAMMING LIBRARY
# 03_MOTORS
# Yiğit YILDIRIM
# 06 - MOTOR BRAKING
# ============================================================

from vex import *


# ============================================================
# 01 - BRAKING NEDİR?
# ============================================================

# Motoru çalıştırmayı bıraktığımızda motorun nasıl
# duracağını belirleyebiliriz.
#
# VEX'te üç temel stopping mode vardır:
#
#     COAST
#     BRAKE
#     HOLD
#
# Bu ayarlar özellikle:
#
#     Drivetrain
#     Intake
#     Lift
#     Arm
#
# gibi mekanizmalarda önemlidir.


motor = Motor(
    Ports.PORT1,
    GearSetting.RATIO_18_1,
    False
)


# ============================================================
# 02 - COAST
# ============================================================

# COAST modunda motor komutla durdurulduğunda
# motor aktif olarak frenlenmez.
#
# Motor kendi hareketiyle bir süre dönmeye devam eder.
#
# Örneğin:

motor.set_stopping(COAST)

motor.spin(FORWARD, 50, PERCENT)

wait(1, SECONDS)

motor.stop()

# COAST:
#
#     Motor komutu durdurulur.
#          ↓
#     Aktif fren uygulanmaz.
#          ↓
#     Motor daha serbest şekilde yavaşlar.
#
# Bu mod, motorun daha yumuşak şekilde durmasının
# istendiği durumlarda kullanılabilir.


# ============================================================
# 03 - BRAKE
# ============================================================

# BRAKE modunda motor durdurulduğunda motor aktif
# şekilde frenlenir.
#
# Örneğin:

motor.set_stopping(BRAKE)

motor.spin(FORWARD, 50, PERCENT)

wait(1, SECONDS)

motor.stop()

# BRAKE:
#
#     Motor komutu durdurulur.
#          ↓
#     Motor frenlenir.
#          ↓
#     Motor COAST'a göre daha hızlı durur.
#
# Bu mod özellikle robotun hareketini daha hızlı
# kesmek istediğimiz durumlarda kullanılabilir.


# ============================================================
# 04 - HOLD
# ============================================================

# HOLD modunda motor durduktan sonra bulunduğu
# pozisyonu korumaya çalışır.
#
# Örneğin bir lift düşünelim:

motor.set_stopping(HOLD)

motor.spin(FORWARD, 50, PERCENT)

wait(1, SECONDS)

motor.stop()

# HOLD:
#
#     Motor durur.
#          ↓
#     Pozisyonunu korumaya çalışır.
#
# Bu nedenle özellikle:
#
#     Lift
#     Arm
#     Pivot
#
# gibi yerçekiminin mekanizmayı hareket ettirebildiği
# sistemlerde kullanışlı olabilir.


# ============================================================
# 05 - STOPPING MODE'U DEĞİŞTİRME
# ============================================================

# set_stopping() motorun durma davranışını belirler.
#
# Örneğin:

motor.set_stopping(COAST)

# veya:

motor.set_stopping(BRAKE)

# veya:

motor.set_stopping(HOLD)

# Bundan sonra motor.stop() çağrıldığında seçilen
# stopping mode kullanılır.
#
# Örneğin:

motor.set_stopping(HOLD)

motor.spin(FORWARD, 50, PERCENT)

wait(1, SECONDS)

motor.stop()

# Burada stop() komutunun kendisi:
#
#     "COAST / BRAKE / HOLD seç"
#
# demez.
#
# Daha önce belirlediğimiz stopping mode'un
# uygulanmasını sağlar.


# ============================================================
# ANAHTAR BİLGİLER
# ============================================================

# Stopping mode ayarlama:
#
#     motor.set_stopping(COAST)
#     motor.set_stopping(BRAKE)
#     motor.set_stopping(HOLD)
#
#
# COAST:
#     Motor aktif olarak frenlenmez.
#
#
# BRAKE:
#     Motor frenlenir.
#
#
# HOLD:
#     Motor durduğu pozisyonu korumaya çalışır.
#
#
# En önemli ilişki:
#
#     set_stopping(...)
#            ↓
#     Durma davranışını belirle
#            ↓
#     motor.stop()
#            ↓
#     Seçilen davranış uygulanır
#
#
# Genel kullanım:
#
#     Drivetrain → COAST / BRAKE
#     Lift       → HOLD
#     Arm        → HOLD
#
# Ancak doğru seçim robotun mekanik tasarımına ve
# sürüş davranışına göre değişebilir.


# ============================================================
# Ders 06 bitti, bir sonraki derse geçin.
# END OF 06 - MOTOR BRAKING
# ============================================================