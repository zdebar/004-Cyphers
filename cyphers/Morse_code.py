import logging
from cyphers.cypher_abstract import SimpleDictionaryEncryption
from utils.helper_functions import invert_dictionary

ENCRYPTION_TEST_STR = "postman"
DECRYPTION_TEST_LIST = ['.--.', '---', '...', '-', '--', '.-', '-.']

MORSE_CODE_DICTIONARY = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MorseCode(SimpleDictionaryEncryption):

    name = "Morse Code"

    def __init__(self):
        super().__init__(MORSE_CODE_DICTIONARY)


if __name__ == "__main__":
    cypher = MorseCode()
    print(cypher.encrypt(ENCRYPTION_TEST_STR))
    print(cypher.decrypt(DECRYPTION_TEST_LIST))
    print(cypher.decrypt("None"))

