import unittest

from CaesarCipher.CaesarCipher import CaesarCipher


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = CaesarCipher()

    def test_a_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("a"), "d")

    def test_w_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("w"), "z")

    def test_x_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("x"), "a")

    def test_z_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("z"), "c")

    def test_abc_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("abc"), "def")

    def test_wxyz_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("wxyz"), "zabc")

    def test_veni_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("veni"), "yhql")

    def test_abc_def_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("abc def"), "def ghi")

    def test_veni_vidi_vici_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("veni vidi vici"), "yhql ylgl ylfl")

    def test_pangram_cipher(self):
        self.assertEqual(self.temp.caesar_cipher("the quick brown fox jumps over the lazy dog"),
                         "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj")

    def test_a_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("d"), "a")

    def test_w_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("z"), "w")

    def test_x_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("a"), "x")

    def test_z_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("c"), "z")

    def test_abc_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("def"), "abc")

    def test_wxyz_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("zabc"), "wxyz")

    def test_veni_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("yhql"), "veni")

    def test_abc_def_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("def ghi"), "abc def")

    def test_veni_vidi_vici_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("yhql ylgl ylfl"), "veni vidi vici")

    def test_pangram_decipher(self):
        self.assertEqual(self.temp.caesar_decipher("wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"),
                         "the quick brown fox jumps over the lazy dog")

    def test_cipher_exception1(self):
        self.assertRaises(ValueError, self.temp.caesar_cipher, 1)

    def test_cipher_exception2(self):
        self.assertRaises(ValueError, self.temp.caesar_cipher, None)

    def test_cipher_exception3(self):
        self.assertRaises(ValueError, self.temp.caesar_cipher, "ą")

    def test_decipher_exception1(self):
        self.assertRaises(ValueError, self.temp.caesar_decipher, 1)

    def test_decipher_exception2(self):
        self.assertRaises(ValueError, self.temp.caesar_decipher, None)

    def test_decipher_exception3(self):
        self.assertRaises(ValueError, self.temp.caesar_decipher, "ą")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()