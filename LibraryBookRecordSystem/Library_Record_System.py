print("***Merhaba CanKitapcılık Hoşgeldiniz***")

def Bilgi_Alma():
    İsimSoyad = input("İsim ve Soyisminiz Nedir?: ")
    Kitap = input("Kütüphanemizden Aldığınız Kitap İsmi Nedir?: ")
    Yazar = input("Kitabın Yazarı Kimdir?: ")
    Tarih = input("Kitabı Aldığınız Tarih ve Vereceğiniz Tarih Nedir?: ")
    Soru = input("Başka Bir Kitap Almak İster Misiniz? (Evet/Hayır): ")

    return İsimSoyad, Kitap, Yazar, Tarih, Soru

def bilgileri_kaydet(İsimSoyad, Kitap, Yazar, Tarih):
    with open("kitap_bilgileri.txt", "a") as dosya:
        dosya.write(f"\nİsim ve Soyisim: {İsimSoyad}\n")
        dosya.write(f"Aldığınız Kitabın İsmi: {Kitap}\n")
        dosya.write(f"Kitabın Yazarı: {Yazar}\n")
        dosya.write(f"Aldığınız Tarih ve Vereceğiniz Tarih: {Tarih}\n\n")

while True:
    İsimSoyad, Kitap, Yazar, Tarih, Soru = Bilgi_Alma()

    print("\nİsim ve Soyisim:", İsimSoyad)
    print("Aldığınız Kitabın İsmi:", Kitap)
    print("Kitabın Yazarı:", Yazar)
    print("Aldığınız Tarih ve Vereceğiniz Tarih:", Tarih)

    bilgileri_kaydet(İsimSoyad, Kitap, Yazar, Tarih)

    if Soru.lower() != "evet":
        break

print("\nTeşekkür ederiz! Bilgileriniz 'kitap_bilgileri.txt' dosyasına kaydedildi.")
