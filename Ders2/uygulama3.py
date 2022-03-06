#kullanıcıdan harf girmesini isteyiniz! E girerse Erkek K girerse Kadın

harf=input("Bir Harf Giriniz E/K:")

if harf == "E" or harf== "e":
    print("Erkek")
elif harf== "K"or harf=="k": #2.veya daha fazla şart olursa elif kullanılır
    print("Kız")
else :
    print("Lütfen E veya K giriniz!")
print("Hoşçakalın...")

