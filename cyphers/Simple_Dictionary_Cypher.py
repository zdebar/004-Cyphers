from cyphers.cypher_abstract import EncryptionMethod
from utils.helper_functions import invert_dictionary
import logging


class SimpleDictionaryEncryption(EncryptionMethod):
    """
    Template for simple encryption methods based on dictionary.
    """
    name = "Simple Dictionary Encryption"

    def __init__(self, encryption_dict: dict):
        self.encryption_key: dict = encryption_dict
        self.decryption_key: dict = invert_dictionary(encryption_dict)
        logging.debug(f"Encryption key: {self.encryption_key}\n"
                      f"Decryption key: {self.decryption_key}")

    def encrypt(self, input_text: str or list) -> list:
        logging.debug(f"Input to encrypt: {input_text}")
        return [self.encryption_key.get(char.upper(), char) for char in input_text if char != " "]

    def decrypt(self, input_text: str or list) -> str:
        logging.debug(f"Input to decrypt: {input_text}")
        return "".join(self.decryption_key.get(char.upper(), char) for char in input_text if char != " ")
