print("""
     Seçeneğiniz Nedir?
     [1] Filtre Kahve
     [2] Espresso
     [3] Sıcak Çikolata
     [4] Mocha
    """)

seker=input("Şeker İstiyor musunuz? E|H : ")
secim=int(input("Kahve Seçiminiz Nedir?  :  "))


if secim==1:
    if seker:
        if seker=="evet":
            print("Şeker İlave Ediliyor...")
        elif seker=="hayır":
            print("Şeker İlave edilmedi Normal Seçiminiz Hazırlanıyor...")
    else:
        print("Şeker İsteği Cevaplanmadı, Şeker Kullanılmıyor")
    print("Seçiminiz Filtre Kahve Hazırlanıyor")
elif secim==2:
    if seker:
        if seker == "evet":
            print("Şeker İlave Ediliyor...")
        elif seker == "hayır":
            print("Şeker İlave edilmedi Normal Seçiminiz Hazırlanıyor...")
    else:
        print("Şeker İsteği Cevaplanmadı, Şeker Kullanılmıyor")
    print("Seçiminiz Espresso Hazırlanıyor")
elif secim==3:
    if seker:
        if seker == "evet":
            print("Şeker İlave Ediliyor...")
        elif seker == "hayır":
            print("Şeker İlave edilmedi Normal Seçiminiz Hazırlanıyor...")
    else:
        print("Şeker İsteği Cevaplanmadı, Şeker Kullanılmıyor")
    print("Seçiminiz Sıcak Çikolata Hazırlanıyor")
elif secim==4:
    if seker:
        if seker == "evet":
            print("Şeker İlave Ediliyor...")
        elif seker == "hayır":
            print("Şeker İlave edilmedi Normal Seçiminiz Hazırlanıyor...")
    else:
        print("Şeker İsteği Cevaplanmadı, Şeker Kullanılmıyor")
    print("Seçiminiz Mocha Hazırlanıyor")
else:
    print("Hatalı Giriş Yaptınız!!!")





