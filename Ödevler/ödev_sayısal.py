import random

klonNumaraları = range (1,90)
sayısal_Sonuc = random.sample(klonNumaraları,6)
while True:
    islem = int(input("""
    Sayısal Loto Lütfen 1-90 arasında sayı giriniz.
    1-Oyna
    2-Sonuç Getir
    3-Çık
    """))
    if islem == 1 :
        kSayi1=int(input("Birinci Sayıyı Giriniz: "))
        kSayi2=int(input("İkinci Sayıyı Giriniz: "))
        kSayi3=int(input("Ücüncü Sayıyı Giriniz: "))
        kSayi4=int(input("Dördüncü Sayıyı Giriniz: "))
        kSayi5=int(input("Besinci Sayıyı Giriniz: "))
        kSayi6=int(input("Altıncı Sayıyı Giriniz: "))
        kListe = [kSayi1,kSayi2,kSayi3,kSayi4,kSayi5,kSayi6]
    elif islem == 2:
        kSonuc = set(kListe)
        sonuc = set(sayısal_Sonuc)
        bilinenSayilar = kSonuc.intersection(sonuc)
        print("Kolonunuzdaki Sayılarınız : ",kListe)
        print("Loto Sonuçları",sayısal_Sonuc)
        if bilinenSayilar == set():
            print("Hiç Sayı bilemediniz.")
        else:
            print(f"Kolonunuzdaki Bildiğiniz Sayilar : {bilinenSayilar}")
    elif islem == 3:
        print("Oyundan Çıktınız.. \nTekrar Görüşmek Üzere...")
        break
else:
    print("Oyundan Çıkıyorsunuz... Tekrar Görüşmek Üzere...")


