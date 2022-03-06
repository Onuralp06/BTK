#kullanıcıdan 5 tane sayı istiyerek en büyük sayıyı listeye atayarak bulunuz!
print("Sıralamak İstediğiniz Sayıları Giriniz!")
sayi1=input("İlk Sayıyı Giriniz:")
sayi2=input("İkicinci Sayıyı Giriniz:")
sayi3=input("Üçüncü Sayıyı Giriniz:")
sayi4=input("Dördücü Sayıyı Giriniz:")
sayi5=input("Beşici Sayıyı Giriniz:")
sayi=[]
sayi.append(sayi1)
sayi.append(sayi2)
sayi.append(sayi3)
sayi.append(sayi4)
sayi.append(sayi5)
sayi.sort()
sayi=[sayi1,sayi2,sayi3,sayi4,sayi5]
print("Yazmış Olduğunuz Sayılar:",sayi)
sayi.sort()
print("Kücükten Büyüğe Sıralaması : ",sayi)
sayi.sort(reverse=True)
print("Büyükten Kücüğe Sıralaması : ",sayi)
print("Girmiş olduğunuz sayıların en büyüğü:",sayi[4])



