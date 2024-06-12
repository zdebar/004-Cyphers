import logging
from cyphers.Simple_Dictionary_Cypher import SimpleDictionaryEncryption
from utils.helper_functions import print_invalid_input, invert_dictionary, ask_for_character_shift

# Encryption and decryption valid for shift = 3
ENCRYPTION_TEST_STR = "postman"
DECRYPTION_TEST_LIST = ['S', 'R', 'V', 'W', 'P', 'D', 'Q']
ENGLISH_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class CaesarCypher(SimpleDictionaryEncryption):

    name = "Caesar cypher"

    def __init__(self) -> None:
        super().__init__(self.create_encryption_dictionary(ENGLISH_ALPHABET, 0))
        logging.debug(self.encryption_key)
        logging.debug(self.decryption_key)

    @staticmethod
    def create_encryption_dictionary(alphabet: str, shift: int) -> dict:
        alphabet_length = len(alphabet)
        negative_shift = alphabet_length - (shift % alphabet_length)
        return {key: alphabet[index-negative_shift] for index, key in enumerate(alphabet)}

    def encrypt(self, input_text: str or list) -> str:
        logging.debug(f"Input to encrypt: {input_text}")

        character_shift = ask_for_character_shift()

        self.encryption_key = self.create_encryption_dictionary(ENGLISH_ALPHABET, character_shift)
        self.decryption_key = invert_dictionary(self.encryption_key)

        return "".join(self.encryption_key.get(char.upper(), char) for char in input_text)

    def decrypt(self, input_text: str or list) -> str:
        logging.debug(f"Input to decrypt: {input_text}")

        character_shift = ask_for_character_shift()

        self.encryption_key = self.create_encryption_dictionary(ENGLISH_ALPHABET, character_shift)
        self.decryption_key = invert_dictionary(self.encryption_key)

        return "".join(self.decryption_key.get(char.upper(), char) for char in input_text)


if __name__ == "__main__":
    cypher = CaesarCypher(3)
    print(cypher.encrypt(ENCRYPTION_TEST_STR))
    print(cypher.decrypt(DECRYPTION_TEST_LIST))


