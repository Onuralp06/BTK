#Sayi Tahmin Oyunu
tuttugumsayi = 5
while True:
    sayi=int(input("Tuttuğum sayıyı giriniz: "))
    if sayi<tuttugumsayi:
        print("Bilemediniz,Sayıyı Büyütünüz")
    elif sayi>tuttugumsayi:
        print("Bildiniz")
    else:
        print("Tebrikler.. Bildin..")
        break


