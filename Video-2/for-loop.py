"""
DÖNGÜLER - FOR DÖNGÜSÜ
"""
#
"""kelime = "python"
for harf in kelime:
    print(harf*3)"""
"""
for değişken_adı in değişken:
    yapılacak işlem"""

"""sayılar = "1953"

for sayı in sayılar:
    print(int(sayı)+2)
"""

"""sayılar = "123456789"

for i in sayılar:
    if i > 3:
        print(i)
"""

tr_harf = "şçöüİı"

parola = input("parolanız:")

for karakter in parola:
    if karakter in tr_harf:
        print("parolada türkçe harfler var.")
        break
    else:
        print("parola uygundur.")
        break
