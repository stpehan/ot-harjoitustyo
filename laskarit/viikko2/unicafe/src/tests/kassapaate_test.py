import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_rahamaara_alustuksessa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_edullisten_lounaiden_maara_alustuksessa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_lounaiden_maara_alustuksessa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    
    def test_edullinen_lounas_kateisella_rahan_maara_kun_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300),60)
    
    def test_edullinen_lounas_kateisella_raha_maara_kun_rahaa_ei_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)

    def test_edullinen_lounas_kateisella_lounas_maara_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_lounas_kateisella_lounas_maara_kun_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukas_lounas_kateisella_rahan_maara_kun_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450),50)
    
    def test_maukas_lounas_kateisella_raha_maara_kun_rahaa_ei_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300),300)

    def test_maukas_lounas_kateisella_lounas_maara_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_lounas_kateisella_lounas_maara_kun_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullinen_lounas_kortilla_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),True)

    def test_edullinen_lounas_kortilla_rahan_maara_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo,760)

    def test_edullinen_lounas_kortilla_lounaiden_maara_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_lounas_kortilla_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)

    def test_edullinen_lounas_kortilla_rahan_maara_kun_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo,200)

    def test_edullinen_lounas_kortilla_lounaiden_maara_kun_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_lounas_kortilla_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),True)

    def test_maukas_lounas_kortilla_rahan_maara_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo,600)

    def test_maukas_lounas_kortilla_lounaiden_maara_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_lounas_kortilla_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),False)

    def test_maukas_lounas_kortilla_rahan_maara_kun_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo,300)

    def test_maukas_lounas_kortilla_lounaiden_maara_kun_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_lisaa_rahaa_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,200)
        self.assertEqual(self.kortti.saldo,1200)

    def test_kortille_lisaa_rahaa_kassan_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100200)
    
    def test_kortille_lisaa_rahaa_negatiivinen_summa_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,-100)
        self.assertEqual(self.kortti.saldo,1000)

    def test_kortille_lisaa_rahaa_negatiivinen_summa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti,-100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
