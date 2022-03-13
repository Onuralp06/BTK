#kullanıcı adı ve şifre alınız. kullanıcı adı olarak "admin" şifre olarakta 123456 girilince "sisteme başarıyla giriş
#yaptınız" yazsın.. yanlış girildikçe "kullanıcı adı ve şifre hatalı yazıp tekrar kullanıcı adı şifre sorsun.


while True :
    kullanici_adi = input("Kullanıcı Adını Giriniz:")
    kullanici_sifre = input("Şifrenizi Giriniz : ")
    if kullanici_adi == "admin" and  kullanici_sifre == "123456":
        break
    else:
        print("Kullanıcı Adı ve Parola Hatalı")
print("Sisteme Başarılı Bir Şekilde Giriş Yaptınız.")



