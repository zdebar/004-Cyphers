import pytest
from cyphers.Caesar_cypher import CaesarCypher


def test_create_encryption_dictionary_positive_shift():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caesar = CaesarCypher()
    shift = 3
    expected_result = {
        'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L',
        'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U',
        'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'
    }
    assert caesar.create_encryption_dictionary(alphabet, shift) == expected_result


def test_create_encryption_dictionary_negative_shift():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caesar = CaesarCypher()
    shift = -3
    expected_result = {
        'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F',
        'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O',
        'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W'
    }
    assert caesar.create_encryption_dictionary(alphabet, shift) == expected_result


def test_create_encryption_dictionary_large_shift():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caesar = CaesarCypher()
    shift = 30
    expected_result = {'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I', 'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M',
                       'J': 'N', 'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S', 'P': 'T', 'Q': 'U', 'R': 'V',
                       'S': 'W', 'T': 'X', 'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C', 'Z': 'D'}
    assert caesar.create_encryption_dictionary(alphabet, shift) == expected_result
