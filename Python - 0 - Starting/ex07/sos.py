import sys


def main():
    try : 
        
        assert len(sys.argv) == 2, "The arguments are bad"
        
        text = sys.argv[1]
        
        assert isinstance(text, str), "The arguments are bad"
        
        text = text.upper()
        NESTED_MORSE = {
            "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
            "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
            "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
            "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
            "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
            "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
            "Y": "-.--",  "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----.",
            " ": "/"  # space between words
        }
        
        for ch in text:
            if ch not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
        
        morse = "".join(NESTED_MORSE[ch] + " " for ch in  text).strip()

        print(morse)
    except AssertionError as e:
        print(f"AssertionError : {e}")


if __name__ == "__main__":
    main()
