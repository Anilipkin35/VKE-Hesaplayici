import os

if __name__ == "__main__":
    # Dosyadaki verileri oku
    with open(os.path.join(os.getcwd(), "input_data.txt"), "r") as f:
        isim_soyisim = f.readline().strip()
        boy = float(f.readline().strip())
        kilo = float(f.readline().strip())

    # Vücut Kitle Endeksi hesaplama
    vke = kilo / (boy ** 2)

    # Durum ve tavsiyeyi belirleme
    if vke < 18.5:
        durum = "Zayıf"
        tavsiye = "Daha fazla protein içeren dengeli bir diyet uygulamalısınız."
    elif 18.5 <= vke < 24.9:
        durum = "Normal"
        tavsiye = "Mevcut yaşam tarzınızı koruyun!"
    elif 25 <= vke < 29.9:
        durum = "Fazla Kilolu"
        tavsiye = "Egzersiz yaparak kilo vermeyi düşünebilirsiniz."
    elif 30 <= vke < 34.9:
        durum = "1. derece obezite"
        tavsiye = "Bir sağlık uzmanına danışarak bir diyet planı oluşturun."
    elif 35 <= vke < 39.9:
        durum = "2. derece obezite"
        tavsiye = "Bir sağlık uzmanına danışarak bir diyet planı oluşturun."
    else:
        durum = "3. derece obezite"
        tavsiye = "Bir sağlık uzmanına danışarak bir diyet planı oluşturun."

    # Sonuçları dosyaya yazma
    dosya_adi = f"{isim_soyisim.replace(' ', '_')}_VKE_Sonuclari.txt"
    dosya_yolu = os.path.join(os.getcwd(), dosya_adi)
    with open(dosya_yolu, "w") as dosya:
        dosya.write(f"İsim ve Soyisim: {isim_soyisim}\n")
        dosya.write(f"Boy: {boy:.2f} m\n")
        dosya.write(f"Kilo: {kilo:.2f} kg\n")
        dosya.write(f"Vücut Kitle Endeksi: {vke:.2f}\n")
        dosya.write(f"Durum: {durum}\n")
        dosya.write(f"Tavsiye: {tavsiye}\n")

    # Sonucu ekrana yazdırma
    print(f"Sonuçlar '{dosya_yolu}' adlı dosyaya kaydedildi.")
    print(f"Dosya yolu: {dosya_yolu}")