import logging
from cyphers.cypher_abstract import SimpleDictionaryEncryption
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


class NATOPhoneticAlphabet(SimpleDictionaryEncryption):

    name = "NATO phonetical alphabet"

    def __init__(self):
        super().__init__(NATO_ALPHABET)


if __name__ == "__main__":
    cypher = NATOPhoneticAlphabet()
    print(cypher.encrypt(ENCRYPTION_TEST_STR))
    print(cypher.decrypt(DECRYPTION_TEST_LIST))
    print(cypher.decrypt("None"))
