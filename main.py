import os

def vke_hesapla(boy, kilo):
    return kilo / (boy ** 2)

def durum_ve_tavsiye(vke):
    if vke < 18.5:
        return "Zayıf", "Daha fazla protein içeren dengeli bir diyet uygulamalısınız."
    elif 18.5 <= vke < 24.9:
        return "Normal", "Mevcut yaşam tarzınızı koruyun!"
    elif 25 <= vke < 29.9:
        return "Fazla Kilolu", "Egzersiz yaparak kilo vermeyi düşünebilirsiniz."
    elif 30 <= vke < 34.9:
        return "1. derece obezite", "Bir sağlık uzmanına danışarak bir diyet planı oluşturun."
    elif 35 <= vke < 39.9:
        return "2. derece obezite", "Bir sağlık uzmanına danışarak bir diyet planı oluşturun."
    else:
        return "3. derece obezite", "Bir sağlık uzmanına danışarak bir diyet planı oluşturun."

def dosya_yaz(isim_soyisim, boy, kilo, vke, durum, tavsiye):
    dosya_adi = f"{isim_soyisim.replace(' ', '_')}_VKE_Sonuclari.txt"
    dosya_yolu = os.path.join(os.getcwd(), dosya_adi)
    with open(dosya_yolu, "w") as dosya:
        dosya.write(f"İsim ve Soyisim: {isim_soyisim}\n")
        dosya.write(f"Boy: {boy:.2f} m\n")
        dosya.write(f"Kilo: {kilo:.2f} kg\n")
        dosya.write(f"Vücut Kitle Endeksi: {vke:.2f}\n")
        dosya.write(f"Durum: {durum}\n")
        dosya.write(f"Tavsiye: {tavsiye}\n")
    return dosya_yolu

def main():
    isim_soyisim = input("İsim ve Soyisim: ")
    boy = float(input("Boyunuzu metre cinsinden girin (ör. 1.75): "))
    kilo = float(input("Kilonuzu girin (kg): "))

    vke = vke_hesapla(boy, kilo)
    durum, tavsiye = durum_ve_tavsiye(vke)

    dosya_yolu = dosya_yaz(isim_soyisim, boy, kilo, vke, durum, tavsiye)

    print(f"Sonuçlar '{dosya_yolu}' adlı dosyaya kaydedildi.")
    print(f"Dosya yolu: {dosya_yolu}")

if __name__ == "__main__":
    main()