import logging
from cyphers.cypher_abstract import EncryptionMethod
from utils.helper_functions import invert_dictionary

ENCRYPTION_TEST_STR = "postman"
DECRYPTION_TEST_LIST = ['Papa', 'Oscar', 'Sierra', 'Tango', 'Mike', 'Alpha', 'November']

NATO_ALPHABET = {
    'A': 'Alpha',   'B': 'Bravo',    'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo',    'F': 'Foxtrot',  'G': 'Golf',    'H': 'Hotel',
    'I': 'India',   'J': 'Juliett',  'K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',    'N': 'November', 'O': 'Oscar',   'P': 'Papa',
    'Q': 'Quebec',  'R': 'Romeo',    'S': 'Sierra',  'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor',   'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'
}

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class NATOPhoneticAlphabet(EncryptionMethod):

    name = "NATO phonetical alphabet"

    def __init__(self):
        self.alphabet_to_nato: dict = NATO_ALPHABET
        self.nato_to_alphabet: dict = invert_dictionary(NATO_ALPHABET)
        logging.debug(f"nato_to_alphabet: {self.nato_to_alphabet}")

    def encrypt(self, to_cypher: str or list) -> list:
        logging.debug(f"Input to encrypt: {to_cypher}")
        return [self.alphabet_to_nato.get(char.upper(), "Invalid character") for char in to_cypher]

    def decrypt(self, input_value: list or str) -> str:
        if isinstance(input_value, list):
            return self.decrypt_list(input_value)
        if isinstance(input_value, str):
            return self.decrypt_str(input_value)

    def decrypt_list(self, input_list: list) -> str:
        return "".join(self.nato_to_alphabet.get(item, "Invalid Input") for item in list(input_list))

    def decrypt_str(self, input_str: str) -> str:
        return NotImplemented


if __name__ == "__main__":
    cypher = NATOPhoneticAlphabet()
    print(cypher.encrypt(ENCRYPTION_TEST_STR))
    print(cypher.decrypt(DECRYPTION_TEST_LIST))
    print(cypher.decrypt("None"))

