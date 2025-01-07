kilo = int(input("Kilo giriniz (kg): "))
boy = float(input("Boy giriniz (m): "))
bki = kilo / (boy**2)

print("Boy Kilo İndeksiniz:", bki)
print("Boy Kilo İndeksinize göre:")

if bki < 18.5:
    print("Zayıfsınız")
elif bki < 24.9:
    print("Normal kilodasınız")
elif bki < 29.9:
    print("Fazla kilolusunuz")
elif bki >= 30:
    print("Obezsiniz")