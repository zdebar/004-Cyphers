import logging
from cyphers.cypher_abstract import SimpleDictionaryEncryption


ENCRYPTION_TEST_STR = "postman"
DECRYPTION_TEST_LIST = ['G', 'F', 'J', 'K', 'D', 'R', 'E']
ENGLISH_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class CaesarCypher(SimpleDictionaryEncryption):

    name = "Caesar cypher"

    def __init__(self):
        super().__init__(self.create_encryption_dictionary(ENGLISH_ALPHABET, 0))
        logging.debug(self.encryption_key)
        logging.debug(self.decryption_key)

    @staticmethod
    def create_encryption_dictionary(alphabet: str, shift) -> dict:
        negative_shift = 26 - (shift % 26)
        logging.debug(negative_shift)
        return {key: alphabet[index-negative_shift] for index, key in enumerate(alphabet)}


if __name__ == "__main__":
    cypher = CaesarCypher()
    print()
    print(cypher.encrypt(ENCRYPTION_TEST_STR))
    print(cypher.decrypt(DECRYPTION_TEST_LIST))
    print(cypher.decrypt("None"))

