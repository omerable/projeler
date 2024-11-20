soru = input("Tam sayılarla işlem için 1, Ondalıklı sayılarla işlem için 2: ")
if soru == "1":
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print("Toplam: ", sayi1 + sayi2)
elif soru == "2":
    sayi1 = float(input("Birinci sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))
    print("Toplam: ", sayi1 + sayi2)
else:
    print("Lütfen 1 veya 2 yazınız")