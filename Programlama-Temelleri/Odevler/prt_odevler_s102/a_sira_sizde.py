# a) Kullanıcı tarafından girilen hava sıcaklığı 5 °C ve altındaysa “Soğuk”; 6-14 °C arasındaysa “Ilık”; 15 °C ve
# daha fazlaysa “Sıcak” çıktılarını veren kodu yazınız.

sicaklik = float(input("Hava sıcaklığını giriniz: "))

sonuc = ""

if sicaklik <= 5:
    sonuc = "Soğuk"
elif 6 <= sicaklik <= 14:
    sonuc = "Ilık"
elif sicaklik >= 15:
    sonuc = "Sıcak"

print(sonuc)