# d) Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boy
# metre cinsinden verilmeli) hesaplayınız.

boy = float(input("Boyunuzu giriniz (m): "))
kilo = int(input("Kilonuzu giriniz (kg): "))

vki = kilo / (boy * boy)
sonuc = ""

########################
if vki < 18:            # bu kısım normalde yok fakat vki 18den küçük olduğunda
    sonuc = "Zayıf"     # boş çıktı veriyordu boş kalmasın diye ekledim
########################
elif 18 <= vki < 25:
    sonuc = "Normal"
elif 25 <= vki < 30:
    sonuc = "Kilolu"
elif 30 <= vki < 35:
    sonuc = "Obez"
elif vki >= 35:
    sonuc = "Ciddi Obez"

print(sonuc)