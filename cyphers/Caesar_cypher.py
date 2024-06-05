import logging
from cyphers.cypher_abstract import SimpleDictionaryEncryption
from random import randint
from utils.helper_functions import invert_dictionary

ENCRYPTION_TEST_STR = "postman"
DECRYPTION_TEST_LIST = ['G', 'F', 'J', 'K', 'D', 'R', 'E']
ENGLISH_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class CaesarCypher(SimpleDictionaryEncryption):

    name = "Caesar cypher"

    def __init__(self):
        super().__init__(self.create_encryption_dictionary(ENGLISH_ALPHABET))
        logging.debug(self.encryption_key)
        logging.debug(self.decryption_key)

    @staticmethod
    def create_encryption_dictionary(alphabet: str) -> dict:
        random_shift = randint(1, len(alphabet))
        logging.debug(random_shift)
        return {key: alphabet[index-random_shift] for index, key in enumerate(alphabet)}


if __name__ == "__main__":
    cypher = CaesarCypher()
    print()
    print(cypher.encrypt(ENCRYPTION_TEST_STR))
    print(cypher.decrypt(DECRYPTION_TEST_LIST))
    print(cypher.decrypt("None"))

