import unittest
import os

# Kodunuzun fonksiyonlarını içeri aktarın
from main import vke_hesapla, durum_ve_tavsiye, dosya_yaz


class TestVKEHesaplayici(unittest.TestCase):

    # vke_hesapla fonksiyonunun test edilmesi
    def test_vke_hesapla(self):
        self.assertEqual(vke_hesapla(1.75, 70), 22.857142857142858)  # Boy 1.75 m, Kilo 70 kg

    # durum_ve_tavsiye fonksiyonunun test edilmesi
    def test_durum_ve_tavsiye(self):
        # VKE 22.86, normal aralıkta olmalı
        durum, tavsiye = durum_ve_tavsiye(22.86)
        self.assertEqual(durum, "Normal")
        self.assertEqual(tavsiye, "Mevcut yaşam tarzınızı koruyun!")

        # VKE 30, 1. derece obezite olmalı
        durum, tavsiye = durum_ve_tavsiye(30)
        self.assertEqual(durum, "1. derece obezite")
        self.assertEqual(tavsiye, "Bir sağlık uzmanına danışarak bir diyet planı oluşturun.")

    # dosya_yaz fonksiyonunun test edilmesi
    def test_dosya_yaz(self):
        # Örnek dosya yazma testi
        isim_soyisim = "Test Kullanıcı"
        boy = 1.75
        kilo = 70
        vke = vke_hesapla(boy, kilo)
        durum, tavsiye = durum_ve_tavsiye(vke)

        # Dosya yazma testini yap
        dosya_yolu = dosya_yaz(isim_soyisim, boy, kilo, vke, durum, tavsiye)

        # Dosya var mı diye kontrol et
        self.assertTrue(os.path.exists(dosya_yolu))

        # Dosya içeriği doğru mu?
        with open(dosya_yolu, "r") as dosya:
            icerik = dosya.read()
            self.assertIn(isim_soyisim, icerik)
            self.assertIn(f"Boy: {boy:.2f} m", icerik)
            self.assertIn(f"Kilo: {kilo:.2f} kg", icerik)
            self.assertIn(f"Vücut Kitle Endeksi: {vke:.2f}", icerik)
            self.assertIn(f"Durum: {durum}", icerik)
            self.assertIn(f"Tavsiye: {tavsiye}", icerik)

        # Test sonrası dosyayı sil
        os.remove(dosya_yolu)


if __name__ == "__main__":
    unittest.main()