print("Merhaba İsminizi yazar mısınz?")
isim = input("İsminizi Giriniz ! ")
print("Hoşgeldin ", isim)
print("Yapmak istediğiniz işlemi yazar mısın?","\nÖrnek : (Toplama/Çıkarma/Çarpma/Bölme)")
cevap = input()

while True:
    if cevap == "toplama" or "Toplama":
        sayi1 =input("Toplamak İstediğiniz 1.sayıyı giriniz : ")
        sayi2 =input("Toplamak İstediğiniz 2.sayıyı giriniz : ")
        print ("Toplamak İstediğiniz Sayıları Sonucu : ", int(sayi1)+int(sayi2))
        soru = input("Başka bir işlem yapmak ister misin?")
    if soru == "evet":
        print("Yapmak istediğin işlemi yazar mısın?")
        cevap = input()
    elif soru == "hayır":
        print("Tekrar Görüşmek üzere")
        break

    if cevap == "çıkarma" or "Çıkarma" or "çıkartma":
        sayi1 =input("Çıkarmak İstediğiniz 1.sayıyı giriniz : ")
        sayi2 =input("Çıkarmak İstediğiniz 2.sayıyı giriniz : ")
        print ("Çıkarmak İstediğiniz Sayıları Sonucu : ", int(sayi1)-int(sayi2))
        soru = input("Başka bir işlem yapmak ister misin?")
    if soru == "evet":
        print("Yapmak istediğin işlemi yazar mısın?")
        cevap = input()
    elif soru == "hayır":
        print("Tekrar Görüşmek üzere")
        break

    if cevap == "çarpma" or "Çarpma":
        sayi1 =input("Çarpmak İstediğiniz 1.sayıyı giriniz : ")
        sayi2 =input("Çarpmak İstediğiniz 2.sayıyı giriniz : ")
        print ("Çarpmak İstediğiniz Sayıları Sonucu : ", int(sayi1)*int(sayi2))
        soru = input("Başka bir işlem yapmak ister misin?")
    if soru == "evet":
        print("Yapmak istediğin işlemi yazar mısın?")
        cevap = input()
    elif soru == "hayır":
        print("Tekrar Görüşmek üzere")
        break

    if cevap == "bölme" or "Bölme":
        sayi1 =input("Bölmek İstediğiniz 1.sayıyı giriniz : ")
        sayi2 =input("Bölmek İstediğiniz 2.sayıyı giriniz : ")
        print ("Bölmek İstediğiniz Sayıları Sonucu : ", int(sayi1)/int(sayi2))
        soru = input("Başka bir işlem yapmak ister misin?")
    if soru == "evet":
        print("Yapmak istediğin işlemi yazar mısın?")
        cevap = input()
    elif soru == "hayır":
        print("Tekrar Görüşmek üzere")
        break

