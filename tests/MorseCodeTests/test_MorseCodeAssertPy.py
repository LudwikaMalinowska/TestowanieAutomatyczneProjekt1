import unittest
from MorseCode.MorseCode import MorseCode
from assertpy import assert_that

class MorseCodeTest(unittest.TestCase):

    def setUp(self):
        self.temp = MorseCode()

    def test_MorseCode_Instance(self):
        assert_that(self.temp).is_instance_of(MorseCode)

    def test_encode_a(self):
        assert_that(self.temp.morse_encode("a")).is_equal_to(".-")

    def test_encode_a_starts_with(self):
        assert_that(self.temp.morse_encode("a")).starts_with('.')

    def test_encode_d(self):
        assert_that(self.temp.morse_encode("d")).is_equal_to("-..")

    def test_encode_d_ends_with(self):
        assert_that(self.temp.morse_encode("d")).ends_with(".")

    def test_encode_n(self):
        assert_that(self.temp.morse_encode("n")).is_equal_to("-.")

    def test_encode_n_starts_with_ends_with(self):
        assert_that(self.temp.morse_encode("n")).starts_with('-').ends_with('.')

    def test_encode_z(self):
        assert_that(self.temp.morse_encode("z")).is_equal_to("--..")

    def test_encode_z_contains(self):
        assert_that(self.temp.morse_encode("z")).contains(".")

    def test_decode_a(self):
        assert_that(self.temp.morse_decode(".-")).is_equal_to("a")

    def test_decode_a_doesnt_contain(self):
        assert_that(self.temp.morse_decode(".-")).does_not_contain("b")

    def test_decode_d(self):
        assert_that(self.temp.morse_decode("-..")).is_equal_to("d")

    def test_decode_d_contain_doesnt_contain(self):
        assert_that(self.temp.morse_decode("-..")).contains("d").does_not_contain("c")

    def test_decode_n(self):
        assert_that(self.temp.morse_decode("-.")).is_equal_to("n")

    def test_decode_z(self):
        assert_that(self.temp.morse_decode("--..")).is_equal_to("z")

    def test_encode_abc(self):
        assert_that(self.temp.morse_encode("abc")).is_equal_to(".- -... -.-.")

    def test_encode_xyz(self):
        assert_that(self.temp.morse_encode("xyz")).is_equal_to("-..- -.-- --..")

    def test_encode_123(self):
        assert_that(self.temp.morse_encode("123")).is_equal_to(".---- ..--- ...--")

    def test_encode_abc_def(self):
        assert_that(self.temp.morse_encode("abc def")).is_equal_to(".- -... -.-.      -.. . ..-.")

    def test_encode_xyz_123(self):
        assert_that(self.temp.morse_encode("xyz 123")).is_equal_to("-..- -.-- --..      .---- ..--- ...--")

    def test_encode_veni_vidi(self):
        assert_that(self.temp.morse_encode("veni vidi")).is_equal_to("...- . -. ..      ...- .. -.. ..")

    def test_encode_pangram(self):
        assert_that(self.temp.morse_encode("the quick brown fox jumps over the lazy dog"))\
            .is_equal_to(
            "- .... .      --.- ..- .. -.-. -.-"
            "      -... .-. --- .-- -.      ..-. --- -..-"
            "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
            "      .-.. .- --.. -.--      -.. --- --."
        )

    def test_encode_special_characters(self):
        special_chars = ",.?;:/-'" + '"' + "_()=+@"
        special_chars_morse = "--..-- .-.-.- ..--.. -.-.-. ---... -..-. -....- .----. .-..-. ..--.- "\
        "-.--. -.--.- -...- .-.-. .--.-."
        assert_that(self.temp.morse_encode(special_chars)).is_equal_to(special_chars_morse)

    def test_decode_abc(self):
        assert_that(self.temp.morse_decode(".- -... -.-.")).is_equal_to("abc")

    def test_decode_xyz(self):
        assert_that(self.temp.morse_decode("-..- -.-- --..")).is_equal_to("xyz")

    def test_decode_123(self):
        assert_that(self.temp.morse_decode(".---- ..--- ...--")).is_equal_to("123")

    def test_decode_abc_def(self):
        assert_that(self.temp.morse_decode(".- -... -.-.      -.. . ..-.")).is_equal_to("abc def")

    def test_decode_xyz_123(self):
        assert_that(self.temp.morse_decode("-..- -.-- --..      .---- ..--- ...--")).is_equal_to("xyz 123")

    def test_decode_veni_vidi(self):
        assert_that(self.temp.morse_decode("...- . -. ..      ...- .. -.. ..")).is_equal_to("veni vidi")

    def test_decode_pangram(self):
        assert_that(self.temp.morse_decode(
            "- .... .      --.- ..- .. -.-. -.-"
            "      -... .-. --- .-- -.      ..-. --- -..-"
            "      .--- ..- -- .---. ...      --- ...- . .-.      - .... ."
            "      .-.. .- --.. -.--      -.. --- --."))\
            .is_equal_to("the quick brown fox jumps over the lazy dog")

    def test_decode_special_characters(self):
        special_chars = ",.?;:/-'" + '"' + "_()=+@"
        special_chars_morse = "--..-- .-.-.- ..--.. -.-.-. ---... -..-. -....- .----. .-..-. ..--.- "\
        "-.--. -.--.- -...- .-.-. .--.-."
        assert_that(self.temp.morse_decode(special_chars_morse)).is_equal_to(special_chars)

    def test_encode_exception1(self):
        assert_that(self.temp.morse_encode).raises(ValueError).when_called_with(1)

    def test_encode_exception2(self):
        assert_that(self.temp.morse_encode).raises(ValueError).when_called_with(None)

    def test_encode_exception3(self):
        assert_that(self.temp.morse_encode).raises(ValueError).when_called_with("ą")

    def test_decode_exception1(self):
        assert_that(self.temp.morse_decode).raises(ValueError).when_called_with(1)

    def test_decode_exception2(self):
        assert_that(self.temp.morse_decode).raises(ValueError).when_called_with(None)

    def test_decode_exception3(self):
        assert_that(self.temp.morse_decode).raises(ValueError).when_called_with("ą")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
