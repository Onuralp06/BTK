import os
while True:
secim = input("Lütfen Seciminizi Giriniz: oluşturma/silmek")
if secim == "oluşturma":
    ad = input("Oluşturmak istediğiniz Klasör Adını Giriniz: ")
    os.mkdir(ad)
elif secim == "silmek":
    ad2 = input("Silmek istediğiniz Klasör Adını Giriniz: ")
    os.rmdir(ad2)

