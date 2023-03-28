import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_saldo_vahenee_oikein_kun_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_saldo_vahenee_oikein_kun_ei_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
