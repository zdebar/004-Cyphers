from typing import Any
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

    def encrypt(self, to_cypher: str or list) -> list:
        logging.debug(f"Input to encrypt: {to_cypher}")
        return [self.encryption_key.get(char.upper(), "Invalid character") for char in to_cypher]

    def decrypt(self, input_value: list or str) -> str:
        if isinstance(input_value, list):
            return self.decrypt_list(input_value)
        if isinstance(input_value, str):
            return self.decrypt_str(input_value)

    def decrypt_list(self, input_list: list) -> str:
        return "".join(self.decryption_key.get(item, "Invalid Input") for item in list(input_list))

    def decrypt_str(self, input_str: str) -> str:
        return NotImplemented
