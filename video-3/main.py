'''
DERS-3 Döngü Araçları ve Listeler
'''

#range(ilk, son)
#range(0, 10)

'''for i in range(0, 10):
    print(i)
'''

'''print(*range(0, 5))'''

'''for i in range(10, 0, -2):
    print(i)
'''

'''for i in range(0, 10):
    if i < 5:
        print("5 ten küçüktür.")
        continue

    else:
        print("5 ten büyüktür")
        break'''

'''while True:
    parola = input("parola belirle: ")

    if not parola:
        print("parola boş olmaz")
    elif len(parola) in range(4, 10):
        print("yeni parolanız :", parola)
        break
    else:
        print("parola 4 ile 10 karakter arasında olmalı")
'''

'''for a in range(1, 15):
    print("-" * a)
'''


'''for i in range(3):
    parola = input("parola belirle: ")

    if not parola:
        pass
    elif len(parola) in range(4, 10):
        print("yeni parolanız :", parola)
        break
    elif i == 2:
        print("parolayı 3 kez yanlış girdin")
        break
    else:
        print("parola 4 ile 10 karakter arasında olmalı")
'''
'''
list = ["elma", "armut", "kiraz"]
for sıra in range(len(list)):
    print("{}.{}".format(sıra, list[sıra]))
'''
'''
list = [3, 4, "dört", [1, 2, 3]]


print(list + ["murat"])'''

'''list = [1, 2, 3]
list.append(4)
print(list)
'''

'''list = [2, 6, 10, 1, 3]
list.sort()
print(list)
'''

liste1 = [1, 2, 3]
liste2 = [4, 5, 6, 7]
yeniliste = [liste1, liste2]
print(yeniliste[0][1])
