import unittest
from MorseCode.MorseCode import MorseCode
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


class MorseCodeParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = MorseCode()

    @parameterized.expand([
        ("a", "._"),
        ("d", "_.."),
        ("n", "_."),
        ("z", "__.."),
        ("abc", "._ _... _._."),
        ("xyz", "_.._ _.__ __.."),
        ("123", ".____ ..___ ...__"),
        ("abc def", "._ _... _._.      _.. . .._."),
        ("xyz 123", "_.._ _.__ __..      .____ ..___ ...__"),
        ("veni vidi", "..._ . _. ..      ..._ .. _.. .."),
        ("the quick brown fox jumps over the lazy dog",
         "_ .... .      __._ .._ .. _._. _._      _... ._. ___ .__ _.      .._. ___ _.._      .___ .._ __ .__. ...      ___ ..._ . ._.      _ .... .      ._.. ._ __.. _.__      _.. ___ __.")

    ])
    def test_one_parameterized(self, text, result):
        self.assertEqual(self.tmp.morse_encode(text), result)

    def tearDown(self):
        self.temp = None


@parameterized([
    ("a", "._"),
    ("d", "_.."),
    ("n", "_."),
    ("z", "__.."),
    ("abc", "._ _... _._."),
    ("xyz", "_.._ _.__ __.."),
    ("123", ".____ ..___ ...__"),
    ("abc def", "._ _... _._.      _.. . .._."),
    ("xyz 123", "_.._ _.__ __..      .____ ..___ ...__"),
    ("veni vidi", "..._ . _. ..      ..._ .. _.. .."),
    ("the quick brown fox jumps over the lazy dog",
     "_ .... .      __._ .._ .. _._. _._      _... ._. ___ .__ _.      .._. ___ _.._      .___ .._ __ .__. ...      ___ ..._ . ._.      _ .... .      ._.. ._ __.. _.__      _.. ___ __.")

])
def test_morse_encode_outside_class(text, result):
    r = MorseCode()
    assert_equal(r.morse_encode(text), result)


@parameterized_class(('text', 'result'), [
    ("a", "._"),
    ("d", "_.."),
    ("n", "_."),
    ("z", "__.."),
    ("abc", "._ _... _._."),
    ("xyz", "_.._ _.__ __.."),
    ("123", ".____ ..___ ...__"),
    ("abc def", "._ _... _._.      _.. . .._."),
    ("xyz 123", "_.._ _.__ __..      .____ ..___ ...__"),
    ("veni vidi", "..._ . _. ..      ..._ .. _.. .."),
    ("the quick brown fox jumps over the lazy dog",
     "_ .... .      __._ .._ .. _._. _._      _... ._. ___ .__ _.      .._. ___ _.._      .___ .._ __ .__. ...      ___ ..._ . ._.      _ .... .      ._.. ._ __.. _.__      _.. ___ __.")

])
class MorseCodeParameterizedPackage2(unittest.TestCase):

    def setUp(self):
        self.tmp = MorseCode()

    def test_one_parameterized(self):
        self.assertEqual(self.tmp.morse_encode(self.text), self.result)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
