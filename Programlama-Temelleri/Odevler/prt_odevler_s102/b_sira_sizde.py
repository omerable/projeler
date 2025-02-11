# b) Bir otoparkın ücret tarifesi aşağıdaki gibidir:
# 1 saate kadar: 5 TL
# 1-5 saat arası: Saat başı 4 TL
# 5 saatten fazla: Saat başı 3 TL
# Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana
# yazdırınız.

saat = int(input("Kaç saat kaldığınızı giriniz: "))

tutar = ""

if saat <= 1:
    tutar=saat*5
elif 1 <= saat <= 5:
    tutar=saat*4
elif saat > 5:
    tutar=saat*3

print("Ödenecek miktar:", tutar)