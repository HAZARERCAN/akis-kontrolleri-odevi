
"""
# 1-12 arası sayı gir
# gelen sayıya göre islami ay adı verisin

ay_sayisi: int = int(input("1-12 aarsı sayı gir:"))
if ( ay_sayisi > 12 ) or ( ay_sayisi < 1 ):
    print("girilen ay sayısı 1-12 aralığında olmalıdır")
elif ay_sayisi == 1:
    print("Muharrem")
elif ay_sayisi == 2:
    print("safer")
elif ay_sayisi == 3:
    print("rebiülevvel")
elif ay_sayisi == 4:
    print("rebiülahir")
elif ay_sayisi == 5:
    print("cemaziyelevvel")
elif ay_sayisi == 6:
    print("cemaziyelahir")
elif ay_sayisi == 7:
    print("recep")
elif ay_sayisi == 8:
    print("saban")
elif ay_sayisi == 9:
    print("ramazan")
elif ay_sayisi == 10:
    print("sevval")
elif ay_sayisi == 11:
    print("zilkade")
elif ay_sayisi == 12:
    print("zilhicce")
"""



"""
# 1-7 arası sayı girilsin.
# gelen sayıya göre islami gün adı verilsin
# ve-and(iki kosul dogru) ya da-or(iki kosuldan herhangi biri dogru olması yeterli)
gun_sayisi: int = int(input("lutfen 1-7 arasında bir sayı giriniz:"))
if (gun_sayisi > 7) or (gun_sayisi < 1):
    print("girmis oldugumuz sayı 7 den  buyuk ve 1 den kucuk olamaz")
elif gun_sayisi == 1:
    print("Yevmu’l-İs̠neyn")
elif gun_sayisi == 2:
    print("Yevmu’s̠-S̠ülās̠ā’")
elif gun_sayisi == 3:
    print("Yevmu’l-Erbi‘ā’")
elif gun_sayisi == 4:
    print("Yevmu’l-Hamīs")
elif gun_sayisi == 5:
    print("Yevmu’l-Cumu'a")
elif gun_sayisi == 6:
    print("Yevmu’s-Sebt")
elif gun_sayisi == 7:
    print("Yevmu’l-Eḥad")
"""




"""
# kullanıcıdan bir sayı alın tek mi çift mi ekrana yazın

sayi: int = int(input("kontrol edilecek sayıyı girin"))
if sayi % 2 == 0:
    print("sayı çifttir")
else:
    print("sayı tektir")
"""

"""
# soru: klavyeden girilen deger 100 den buyukse karesini, küçükse küpünü, eşit ise ekrana yaz

sayi: int = int(input("sayı gir"))
if sayi > 100:
    print(sayi ** 2)
elif sayi < 100:
    print(sayi ** 3)
else:
    print("sayı 100'e esittir")
"""


"""
# kullanıcıdan alınan sayının aralıgını belirieyiniz
#  0-10  11-20
sayi: int = int(input("sayı gir"))
if 0 < sayi and sayi < 11:
    print("sayı 0-11 aralığındadır")
elif 10 < sayi and sayi < 21:
    print("sayı 11-21 aralığındadır")
"""




"""
ÖDEV:  Kullanıcıdan vize final not girilmesi istensin
not aralığı 0 ile 100 arasında olmalıdır.
# vize ve finalin ortalaması alınsın.
# 0-44 : Kaldınız
# 45-69: Geçtiniz
# 70-84: İyi
# 85-100: Pekiyi
"""

"""
vize_not:float = float(input("vize notu:"))
final_not:float = float(input("final notu:"))

if ( 0 <= vize_not <= 100 ) and ( 0 <= final_not <= 100 ):
    # ortalama= vize %40 final %60
    ortalama: float = (vize_not * 0.4) + (final_not * 0.6)
    print(ortalama)
    if 0 <= ortalama < 45:
        print(f"ortalamanız: {ortalama}  dersten kaldınız")
    elif 45 <= ortalama < 70:
        print(f"ortalamanız: {ortalama}  dersten geçtiniz")
    elif 70 <= ortalama < 85:
        print(f"ortalamanız: {ortalama}  dersten iyi notla geçtiniz")
    else:
        print(f"ortalamanız: {ortalama}  dersten pekiyi notla geçtiniz")

else:
    print("vize ve final notu 0-100 aralığında olmalıdır.")
"""


# Kullanıcı Gİriş Paneli Tasarlayınız.

"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""

"""
kullanici_adi = "hazarercan"
email = "hazar_ercan@hotmail.com"
sifre = "123456"

print("..........................GİRİŞ PANELİ......................")
user_name_or_email: str = input("lütfen kullanıcı adı veya email giriniz.")
password: str = input("lutfen şifrenizi giriniz.")

if ( kullanici_adi == user_name_or_email or user_name_or_email == email ) and ( password == sifre):
    print("giriş basarili")
else:
    cevap: str = input("kayıt olamk ister misiniz (E/H):").upper()

    if cevap == "E":
        ad = input("adınız:")
        soyad = input("soyadınız:")
        username = input("kullanıcı adınız:")
        email_user = input("email adresiniz:")
        password_user = input("şifreniz:")
        password_user_control = input("şifrenizi tekrar girniz:")

        if password_user == password_user_control:
            print("hoşgeldiniz")
            print(f"ad: {ad}, soyad: {soyad}, kullanıcı adı: {username}, email: {email_user}, şifre: {password_user}")
        else:
            print("şifreler birbirini tutmuyor!")

    elif cevap == "H":
        print("peki :)")
    else:
        print("yanlış seçim")
"""

"""
# girilen 3 sayıyı buyukluk olarak karsılastıren python uygulamasını yapınız

a: int = int(input("a sayısını giriniz:"))
b: int = int(input("b sayısını giriniz:"))
c: int = int(input("c sayısını giriniz:"))

if a > b and a > c :
    print("a en buyuk sayı")
elif b > a and b > c:
    print("b en buyuk sayı")
else:
    print("c en buyuk sayı")
"""






















