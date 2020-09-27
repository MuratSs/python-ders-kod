masraf = 10
gün = 5
hafta = 4
print(hafta * gün * 3 * masraf)

a = 4
print(a*a)

dolar = 7.64
tl = 200
euro = 8.30
kademe = tl/dolar
print(tl / dolar)
print(tl / euro)

a = 18
print("hello", "world", sep="!")

print("murat", "mirgün", "ercan", sep="-")


print("hello\nworld")
print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")

print(*"merhaba")

print("merhaba\tarkadaşlar")
print("\"selam\" kelimesi \"merhabala\" ile aynıdır")

print("\a" * 10)

print("merhaba\rPhyton dersine")
print("merhaba\rdünya")
print("düşey\vsekme")
print("gmail.com\b.tr")

a = 10
b = 10.5

c = "hello"

print(type(c))


pi = 3.14
print("alan hesabı")
yaricap = float(input("yarıçapı gir:"))
print(pi * yaricap * yaricap)

sayı = int(input("sayı gir : "))
tip = type(sayı)
print(tip)


karakter = "10"
sayi = int(karakter)
print(type(karakter))
print(type(sayi))


vari = input("lütfen bir sayı girin:")
sayi = int(vari)
print("karesi : ", sayi ** 3)


sayı = 10
yazı = str(sayı)
print(type(yazı))


sayı = 10234
yazı = str(sayı)
print(len(yazı))

print(len(str(1938)))

a = 23
b = float(a)
print(b)

a = 23.2
print(a)
print(int(a))

a = 12+0j
print(type(a))
print(complex(15))

veri = int(input("bir sayı gir:"))
print(type(veri))

sayı = 23
sayı2 = 27
a = int(input("derece girin"))
if a < sayı:
    print("hava soğuk")

elif sayı2 > a > sayı:
    print("hava ılık")
else:
    print("hava sıcak")


ad = "abs"
password = int(1234)

a = str(input("ad girin:"))
b = int(input("şifre girin"))

if ((ad == a) and (password == b)):
    print("giriş başarılı")
else:
    print("hatalı giriş")
