from abc import ABC, abstractmethod
import logging
from utils.helper_functions import invert_dictionary


logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class EncryptionMethod(ABC):

    name = None

    @abstractmethod
    def encrypt(self, input_str: str or list):
        return NotImplemented

    @abstractmethod
    def decrypt(self, input_str: str or list):
        return NotImplemented


class SimpleDictionaryEncryption(EncryptionMethod):

    name = "Simple Dictionary Encryption"

    def __init__(self, encryption_dict: dict):
        self.encryption_key: dict = encryption_dict
        self.decryption_key: dict = invert_dictionary(encryption_dict)
        logging.debug(f"nato_to_alphabet: {self.decryption_key}")

    @staticmethod
    def _validate_input(input_value):
        if not isinstance(input_value, (str, list)) or not input_value:
            raise ValueError("Input must be a non-empty string or list")

    def encrypt(self, to_cypher: str or list) -> list:
        self._validate_input(to_cypher)
        logging.debug(f"Input to encrypt: {to_cypher}")
        return [self.encryption_key.get(char.upper(), "'Invalid Input'") for char in to_cypher if char != " "]

    def decrypt(self, input_value: list or str) -> str:
        self._validate_input(input_value)
        logging.debug(f"Input to encrypt: {input_value}")
        if isinstance(input_value, list):
            return self.decrypt_list(input_value)
        if isinstance(input_value, str):
            return NotImplemented

    def decrypt_list(self, input_list: list) -> str:
        return "".join(self.decryption_key.get(item, "'Invalid Input'") for item in list(input_list))
