#kullanıcıdan ad soyad telefon alarak bilgiler adlı listeye atayınız!
bilgiler =[]#boş bir liste tanımlar

isim=input("Lütfen adınızı giriniz:")#Kullanıcıdan ismini girmesi istenmiştir.
soyisim=input("Lütfen soyadınızı giriniz:")#Kullanıcıdan soyisimini girmesi istenmiştir.
telefon_numarası=input("Cep Telefon numaranızı giriniz:")#Kullanıcıdan Telefon Numarası girmesi istenmiştir.

bilgiler.append(isim)
bilgiler.append(soyisim)
bilgiler.append(telefon_numarası)
bilgiler=[isim,soyisim,telefon_numarası]
print("Vermiş olduğunuz bilgiler için teşekkür ederiz.")
print("\n")
print("Yazmış olduğunuz bilgiler;")
print("Adınız:",bilgiler[0],"\nSoyadınız:",bilgiler[1],"\nTelefon Numaranız:",bilgiler[2])
print(bilgiler)

