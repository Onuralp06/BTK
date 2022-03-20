#Sayi Tahmin Oyunu
import random
while True:
    seviye = input("Bir seviye seçiniz : kolay/orta/zor")
    if seviye == "kolay":
        uret=random.randint(1,10)
        break
    elif seviye == "orta":
        uret=random.randint(1,50)
        break
    elif seviye == "zor":
        uret=random.randint(1,100)
        break
    else:
        print("Lütfen Doğru Bir Seçim Giriniz!")
while True:
    tahmin=int(input("Bir Tahminde Bulununuz: "))
    if tahmin<uret:
        print("Sayınızı Büyütünüz.")
    elif tahmin>uret:
        print("Sayınızı Küçültünüz")
    else:
        print("Tebrikler Doğru Bildiniz.")
        break