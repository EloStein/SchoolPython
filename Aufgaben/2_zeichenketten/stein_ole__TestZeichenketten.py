import unittest
from . import stein_ole__zeichenketten

class TestZeichenketten(unittest.TestCase):

    def testZaehleA(self):
        self.assertEqual(stein_ole__zeichenketten.zaehleA("Hallo"), 1)
        self.assertEqual(stein_ole__zeichenketten.zaehleA("Abab"), 2)
        self.assertEqual(stein_ole__zeichenketten.zaehleA("Anna"), 2)

    def testZaehle(self):
        self.assertEqual(stein_ole__zeichenketten.zaehle("OleOhneKohle", "o"), 3)
        self.assertEqual(stein_ole__zeichenketten.zaehle("Yarak", "a"), 2)
        self.assertEqual(stein_ole__zeichenketten.zaehle("Nutty Putty", "y"), 2)

    def testZaehleVokale(self):
        self.assertEqual(stein_ole__zeichenketten.zaehleVokale("Aeiou"), 5)
        self.assertEqual(stein_ole__zeichenketten.zaehleVokale("Anna"), 2)
        self.assertEqual(stein_ole__zeichenketten.zaehleVokale("Scary Juan in Sacramento"), 8)

    def testEntferneLeerzeichen(self):
        self.assertEqual(stein_ole__zeichenketten.entferneLeerzeichen("Y R U"), "Y_R_U")
        self.assertEqual(stein_ole__zeichenketten.entferneLeerzeichen("Huan der Mendez"), "Huan_der_Mendez")
        self.assertEqual(stein_ole__zeichenketten.entferneLeerzeichen("Frau Hell die unfreundliche_"), "Frau_Hell_die_unfreundliche_")

    def testStretch(self):
        self.assertEqual(stein_ole__zeichenketten.stretch("Hello World"), "H_e_l_l_o__W_o_r_l_d")
        self.assertEqual(stein_ole__zeichenketten.stretch("A A_"), "A__A__")

    def testVertausche(self):
        self.assertEqual(stein_ole__zeichenketten.vertausche("abc"), "ABC")
        self.assertEqual(stein_ole__zeichenketten.vertausche("AbAbAbAb"), "aBaBaBaB")

    def testAufAb(self):
        self.assertEqual(stein_ole__zeichenketten.aufAb("abcd"), "AbCd")
        self.assertEqual(stein_ole__zeichenketten.aufAb("HALLO MENDEZ"), "HaLlO MeNdEz")
        self.assertEqual(stein_ole__zeichenketten.aufAb("OleOleOle"), "OlEoLeOlE")

    def testAufAbAnzahl(self):
        self.assertEqual(stein_ole__zeichenketten.aufAbAnzahl("abcd", 2), "aBcD")
        self.assertEqual(stein_ole__zeichenketten.aufAbAnzahl("HALLO MENDEZ", 3), "haLlo meNdeZ")
        self.assertEqual(stein_ole__zeichenketten.aufAbAnzahl("OleOleOle", 1), "OLEOLEOLE")


    def testVerschiebe(self):
        self.assertEqual(stein_ole__zeichenketten.verschiebe("A" ), "D")
        self.assertEqual(stein_ole__zeichenketten.verschiebe("Z" ), "C")

    def testVerschiebung2(self):
        self.assertEqual(stein_ole__zeichenketten.verschiebe2("A", "D"), "D")
        self.assertEqual(stein_ole__zeichenketten.verschiebe2("Z", "D"), "C")

if __name__ == '__main__':
    unittest.main()