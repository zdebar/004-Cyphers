import pytest
from cyphers.Simple_Dictionary_Cypher import SimpleDictionaryEncryption


def test_simple_dictionary_encryption_encrypt():
    encryption_dict = {'A': '1', 'B': '2', 'C': '3'}
    sde = SimpleDictionaryEncryption(encryption_dict)
    assert sde.encrypt("ABC") == ['1', '2', '3']
    assert sde.encrypt(['A', 'B', 'C']) == ['1', '2', '3']
    assert sde.encrypt("ABX") == ['1', '2', 'X']


def test_simple_dictionary_encryption_decrypt_list():
    encryption_dict = {'A': '1', 'B': '2', 'C': '3'}
    sde = SimpleDictionaryEncryption(encryption_dict)
    assert sde.decrypt(['1', '2', '3']) == "ABC"
    assert sde.decrypt(['1', '2', 'X']) == "ABX"


def test_simple_dictionary_encryption_decrypt_str():
    encryption_dict = {'A': '1', 'B': '2', 'C': '3'}
    sde = SimpleDictionaryEncryption(encryption_dict)
    assert sde.decrypt("123") == "ABC"
