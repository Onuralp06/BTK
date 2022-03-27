#Dikdörtgenin alanını ve çevresini hesaplayan 2 ayrı fonksiyon yazınız. Kullanıcıdan aldığınız değere göre
#alanı ve çevreyi ekrana yazdırınız.

def alan (kisa,uzun):
    return (kisa+uzun)*2
def cevre (kisa,uzun):
    return kisa*uzun
kisa=int(input("Kısa kenarı giriniz: "))
uzun=int(input("Uzun kenarı giriniz: "))
print("Dikdörtgenin çevresi : ",cevre(kisa,uzun))
print("Dikdörtgenin alanı : ",alan(kisa,uzun))









