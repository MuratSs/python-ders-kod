"""
while loop
"""


"""a = 10
b = 5
while b < a:
    b = b + 1
    print(b)
"""


karşılama = """
(1) toplama
(2) çıkartma
(3) çarpma 
(4) bölme
"""

"""
print(karşılama)

anahtar = 1

while anahtar == 1:
    soru = input("işlemi seçin?")

    if soru == "q":
        print("çkılıyor..")
        anahtar = 0

    elif soru == "1":
        sayı1 = int(input("İlk Sayıyı girin:"))
        sayı2 = int(input("ikinci sayıyı girin:"))
        print("{} sayısı ile {} sayısının toplamı: {}".
              format(sayı1, sayı2, sayı1+sayı2))
    elif soru == "2":
        sayı1 = int(input("İlk Sayıyı girin:"))
        sayı2 = int(input("ikinci sayıyı girin:"))
        print("{} sayısı ile {} sayısının çıkartılmış hali: {}".
              format(sayı1, sayı2, sayı1+sayı2))

    elif soru == "3":
        sayı1 = int(input("İlk Sayıyı girin:"))
        sayı2 = int(input("ikinci sayıyı girin:"))
        print("{} sayısı ile {} sayısının çarpımı: {}".
              format(sayı1, sayı2, sayı1+sayı2))

    elif soru == "4":
        sayı1 = int(input("İlk Sayıyı girin:"))
        sayı2 = int(input("ikinci sayıyı girin:"))
        print("{} sayısı ile {} sayısının bölümü: {}".
              format(sayı1, sayı2, sayı1+sayı2))
    else:
        print("geçersiz işlem")
"""

"""kullanıcıadı = "root"
password = "root"

giriş_hakkı = 3
while True:  # kullanıcı doğru giriş yaptığında sona ersin
    kullanıcı_adı = input("Kullanıcı adınız")
    şifre = input("şifreniz:")

    if (kullanıcıadı != kullanıcı_adı and şifre == password):
        print("Kullanıcı adı hatalı")
        giriş_hakkı -= 1
    elif (kullanıcıadı == kullanıcı_adı and şifre != password):
        print("şifre hatalı")
        giriş_hakkı -= 1
    elif (kullanıcıadı != kullanıcı_adı and şifre != password):
        print("bilgiler hatalı")
        giriş_hakkı -= 1
    else:
        print("giriş başarılı")
        break
    if (giriş_hakkı == 0):
        print("giriş hakkın bitti")
        break
"""


"""

print(
    """
# İşlemler:
# 1 - bakiye sorgu
# 2 - para yatırma
# 3 - para çekme
#q - çıkış
"""
)
bakiye = 1000

while True:
    işlem = input("İşlemi girin : ")

    if(işlem == "q"):
        print("işlem kapatılıyor")
        break
    elif (işlem == "1"):
        print("bakiyeniz {} tldir.".format(bakiye))
    elif (işlem == 2):
        ekleme = int(input("Yatırmak istediğiniz tutar"))
        bakiye += ekleme
    elif (işlem == 3):
        çekme = int(input("Çekmek İstediğiniz Tutar:"))
        if (bakiye - çekme < 0):
            print("Bakiye yetersizdir.")
            print("bakiyeniz {} tldir.".format(bakiye))
            continue

        bakiye -= çekme
    else:
        print("geçersiz işlem")
        break

"""


"""while True:
    sayi = input("sayı: ")
    if (sayi == "q"):
        print("programdan çıkılıyor")
        break

    sayi = int(sayi)

    faktoriyel = 1
    for i in range(2, sayi+1):
        faktoriyel *= i
    print("Fkatoriyeli:", faktoriyel)
"""
