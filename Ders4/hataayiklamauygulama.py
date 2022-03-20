#kullanıcıdan bir sayi isteyin..
#sayi girmediğinde tekrar tekrar sayi girmesini isteyen,
#sayi girdiğinde de ekrana sayının karesini yazdıran program
while True:
    try:
        sayi = int(input("Lütfen bir sayı giriniz:"))
        break
    except ValueError:
        print("Yanlış Girdiniz Lütfen Sayı Giriniz.")
print("Girdiğiniz Sayının Karesi: ",sayi**2)








