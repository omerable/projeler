# Girilen üç sayıdan en büyüğünü bulan kodu yazınız

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))

eb = sayi1

if sayi2 > eb:
    eb = sayi2
elif sayi3 > eb:
    eb = sayi3

print(eb)