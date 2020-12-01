import unittest
from CaesarCipher.CaesarCipher import CaesarCipher
from assertpy import assert_that


class CaesarTest(unittest.TestCase):

    def setUp(self):
        self.temp = CaesarCipher()

    def test_Caesar_Instance(self):
        assert_that(self.temp).is_instance_of(CaesarCipher)

    def test_encode_a(self):
        assert_that(self.temp.caesar_cipher("a")).is_equal_to("d")

    def test_encode_w(self):
        assert_that(self.temp.caesar_cipher("w")).is_equal_to("z")

    def test_encode_x(self):
        assert_that(self.temp.caesar_cipher("x")).is_equal_to("a")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
