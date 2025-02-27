import unittest
from AffineCipher.AffineCipher import AffineCipher
from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher


class AffineTest(unittest.TestCase):

    def setUp(self):
        self.temp = AffineCipher()

    def test_encode_a_equal(self):
        assert_that(self.temp.affine_cipher("a", 1, 3), equal_to("d"))

    def test_encode_z_equal(self):
        assert_that(self.temp.affine_cipher("z", 1, 3), equal_to("c"))

    def test_encode_abc_equal(self):
        assert_that(self.temp.affine_cipher("abc", 3, 12), equal_to("mps"))

    def test_encode_veni_vidi_equal(self):
        assert_that(self.temp.affine_cipher("veni vidi", 3, 12), equal_to("xyzk xkvk"))

    def test_encode_pangram_equal(self):
        assert_that(self.temp.affine_cipher("the quick brown fox jumps over the lazy dog", 3, 12),
                    equal_to("rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce"))

    def test_decipher_a_equal(self):
        assert_that(self.temp.affine_decipher("d", 1, 3), equal_to("a"))

    def test_decipher_z_equal(self):
        assert_that(self.temp.affine_decipher("c", 1, 3), equal_to("z"))

    def test_decipher_abc_equal(self):
        assert_that(self.temp.affine_decipher("mps", 3, 12), equal_to("abc"))

    def test_decipher_veni_equal(self):
        assert_that(self.temp.affine_decipher("xyzk", 3, 12), equal_to("veni"))

    def test_decipher_veni_vidi_equal(self):
        assert_that(self.temp.affine_decipher("xyzk xkvk", 3, 12), equal_to("veni vidi"))

    def test_decipher_pangram_equal(self):
        assert_that(self.temp.affine_decipher("rhy iuksq plcaz bcd nuwfo cxyl rhy tmjg vce", 3, 12),
                    equal_to("the quick brown fox jumps over the lazy dog"))

    def test_cipher_exception1(self):
        assert_that(calling(self.temp.affine_cipher).with_args(1, 1, 3), raises(ValueError))

    def test_cipher_exception2(self):
        assert_that(calling(self.temp.affine_cipher).with_args(None, 1, 3), raises(ValueError))

    def test_cipher_exception3(self):
        assert_that(calling(self.temp.affine_cipher).with_args("ą", 1, 3), raises(ValueError))

    def test_cipher_exception4(self):
        assert_that(calling(self.temp.affine_cipher).with_args("abc", -1, 3), raises(ValueError))

    def test_cipher_exception5(self):
        assert_that(calling(self.temp.affine_cipher).with_args("abc", 3, -12), raises(ValueError))

    def test_cipher_exception6(self):
        assert_that(calling(self.temp.affine_cipher).with_args("abc", "3", 12), raises(ValueError))

    def test_cipher_exception7(self):
        assert_that(calling(self.temp.affine_cipher).with_args("abc", 3, "12"), raises(ValueError))

    def test_decipher_exception1(self):
        assert_that(calling(self.temp.affine_decipher).with_args(1, 1, 3), raises(ValueError))

    def test_decipher_exception2(self):
        assert_that(calling(self.temp.affine_decipher).with_args(None, 1, 3), raises(ValueError))

    def test_decipher_exception3(self):
        assert_that(calling(self.temp.affine_decipher).with_args("ą", 1, 3), raises(ValueError))

    def test_decipher_exception4(self):
        assert_that(calling(self.temp.affine_decipher).with_args("abc", -1, 3), raises(ValueError))

    def test_decipher_exception5(self):
        assert_that(calling(self.temp.affine_decipher).with_args("abc", 3, -12), raises(ValueError))

    def test_decipher_exception6(self):
        assert_that(calling(self.temp.affine_decipher).with_args("abc", "3", 12), raises(ValueError))

    def test_decipher_exception7(self):
        assert_that(calling(self.temp.affine_decipher).with_args("abc", 3, "12"), raises(ValueError))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
