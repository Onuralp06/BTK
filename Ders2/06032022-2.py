liste=[]#boş bir liste tanımlar
liste=["Elma","Armut",20] #artık listenin elemanları değişti!
sayilar=[15,19,2,3,8,25,6]
isimler=["ali","veli","ahmet","zehra","hatice"]
gunler=["Pazartesi","Salı","Çarşamba"]
print(gunler)
print("0. indeksdeki eleman:",gunler[0]) #ctrl+d çoğaltır , ctrl+y satırı siler
print(gunler[1])
print(gunler[2])
gunler.append("Perşembe") #append:yeni eleman ekler
print(gunler)
print("Eleman Sayısı:",len(gunler)) #len: listenin eleman sayısını verir
gunler.pop()#hiçbirşey yazılmadığında listenin son elemanı çıkarır.
print(gunler)
print("Eleman Sayısı:",len(gunler)) #len: listenin eleman sayısını verir
gunler.pop(0)#hiçbirşey yazılmadığında listenin son elemanı çıkarır.
print(gunler)
print("Gün Sayısı:",len(gunler)) #len: listenin eleman sayısını verir
print(sayilar)
sayilar.sort()#(varsayılan(default) hiçbirşey yazılmaz ise kücükten büyüğe sıralanır.
print("Küçükten büyüğe sıralama",sayilar)
sayilar.sort(reverse=True) #büyükten kücüğe doğru sıralamaktadır.
print("Büyükten küçüğe sıralama",sayilar)
isimler.sort()
print(isimler)
isimler.sort(reverse=True)
print(isimler)



