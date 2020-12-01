
class CaesarCipher:
    letters = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,

        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
        "k": 10,
        "l": 11,
        "m": 12,
        "n": 13,
        "o": 14,
        "p": 15,
        "q": 16,
        "r": 17,
        "s": 18,
        "t": 19,
        "u": 20,
        "v": 21,
        "w": 22,
        "x": 23,
        "y": 24,
        "z": 25
    }

    reverse_letters = {v: k for k, v in letters.items()}

    def caesar_cipher(self, text):
        # return self.reverse_letters[self.letters[text] + 3]

        letterNr = self.letters[text]
        letterNr += 3
        if letterNr > 25:
            letterNr -= 26

        return self.reverse_letters[letterNr]


    def caesar_decipher(self, caesar_text):
        ...

