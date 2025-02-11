# Kullanıcıdan adını, maaşını ve çalışma yılını girmesini isteyiniz. 0-5 yıl arası çalışanlara %10; 6-10 yıl arası 
# çalışanlara %15; 11 ve daha fazla yıl çalışanlara %25 zam yapılmaktadır. Buna göre “Sayın …………….., zamlı
# maaşınız …….. TL” çıktısı veren kodu yazınız.

ad = input("Adınızı giriniz: ")
maas = int(input("Maaşınızı giriniz: "))
yil = int(input("Çalışma yılınızı giriniz: "))

if 1 <= yil <= 5:
    maas = (maas*0.10) + maas
elif 6 <= yil <= 10:
    maas = (maas*0.15) + maas
elif yil >= 11:
    maas = (maas*0.25) + maas

print(f"Sayın {ad}, zamlı maaşınız {maas} TL")