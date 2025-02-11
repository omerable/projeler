# c) Üçgenler kenar uzunluklarına göre üçe ayrılmaktadır: Eşkenar, İkizkenar ve Çeşitkenar. Kullanıcının girdiği
# 3 kenar uzunluğuna göre üçgenin türünü ekrana yazdırınız.

kenar1 = int(input("1. Kenar uzunluğu: "))
kenar2 = int(input("2. Kenar uzunluğu: "))
kenar3 = int(input("3. Kenar uzunluğu: "))

sonuc = ""

kenartop = kenar1 + kenar2 + kenar3 

if kenartop > 180 or kenartop < 180:
    sonuc = "Bu bir üçgen değil!"
elif kenar1 == kenar2 == kenar3:
    sonuc = "Eşkenar"
elif kenar1 == kenar2 or kenar2 == kenar3 or kenar1 == kenar3:
    sonuc = "İkizkenar"
else:
    sonuc = "Çeşitkenar"

print(sonuc)