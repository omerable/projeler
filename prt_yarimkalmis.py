a = ["B", "İ", "L", "İ", "Ş", "İ", "M"]
ders = ["matematik", "programlama temelleri", "bilişim", "edebiyat"]
sayilar = [35, 26, 81, 64]
ondalikli_sayilar = [1.4, 6.8]

def a1():
    a.sort()
    print(a)
def b1():
    a.sort(reverse=1)
    print(a)
def c1():
    print(a.count("İ"))
def ch1():
    a.pop(5)
    a.pop(4)
    print(a)
def d1():
    ders_copy = ders.copy()
    print(ders_copy)
def e1():
    ders.clear()
    print(ders)
def f1():
    print(a.index("L"))
def a2():
    sayilar.sort()
    print(sayilar)
def b2():
    sayilar.sort(reverse=1)
    print(sayilar)
def c2():
    print(sayilar.count(26))
def ch2():
    sayilar.remove(26)
    print(sayilar)
def d2():
    sayilar.clear()
    print(sayilar)
def e2():
    print(sayilar.index(35))
def f2():
    yenisayilar = sayilar+ondalikli_sayilar
    print(yenisayilar)

a1()
b1()
c1()
ch1()
d1()
e1()
f1()
a2()
b2()
c2()
ch2()
d2()
e2()
f2()
