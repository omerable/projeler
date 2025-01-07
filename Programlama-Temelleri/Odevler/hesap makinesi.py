def toplama():
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print("Cevap:",sayi1+sayi2)
    
def carpma():
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print("Cevap:",sayi1*sayi2)
    
def cikarma():
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print("Cevap:",sayi1-sayi2)
    
def bolme():
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    print("Cevap:",sayi1/sayi2)

while True:
    print(r"""1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme

Çıkış için 'q' tuşuna basınız.
""")
    soru = input("Hangi işlemi yapacaksınız?: ")

    if soru == "q":
        break
    elif soru == "1":
        toplama()
        break
    elif soru == "2":
        cikarma()
        break
    elif soru == "3":
        carpma()
        break
    elif soru == "4":
        bolme()
        break
    else:
        print("Lütfen geçerli bir işlem seçiniz!")
    