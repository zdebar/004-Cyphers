from abc import ABC, abstractmethod
from typing import Any


class EncryptionMethod(ABC):

    name = None

    @abstractmethod
    def encrypt(self, input_str: Any):
        return NotImplemented

    @abstractmethod
    def decrypt(self, input_str: Any):
        return NotImplemented

    def ask_for_additional_input(self):
        return NotImplemented
