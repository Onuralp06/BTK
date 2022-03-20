#print(a) #nameerror hatası verir
# print("Btk"deneme)#syntaxError hatası verir
# print(10/0)# zeroDivisionError hatası verir
# int("5a")#valueError Hatası verir
try:
    sayi=int(input("Bir Sayı Giriniz: "))
    sayi2=int(input("Bir Sayı Giriniz"))
    print("Bölüm: ",sayi/sayi2)
except ValueError:
    print("Lütfen Bir Sayi Gir! Harf Girme!")
except ZeroDivisionError:
    print("0'a bölme yapılamaz!")
except SyntaxError:
    print("Yazım hatası var!")
except NameError:
    print("Böyle bir değişken yok")
except:
    print("Genel hata oluştu.")
print("Program buradan çalışmasına devam eder...")
