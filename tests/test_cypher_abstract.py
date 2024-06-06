import pytest
from cyphers.cypher_abstract import EncryptionMethod, SimpleDictionaryEncryption


def test_abstract_class_instantiation():
    with pytest.raises(TypeError):
        EncryptionMethod()


def test_simple_dictionary_encryption_encrypt():
    encryption_dict = {'A': '1', 'B': '2', 'C': '3'}
    sde = SimpleDictionaryEncryption(encryption_dict)
    assert sde.encrypt("ABC") == ['1', '2', '3']
    assert sde.encrypt(['A', 'B', 'C']) == ['1', '2', '3']
    assert sde.encrypt("ABX") == ['1', '2', "'Invalid Input'"]


def test_simple_dictionary_encryption_decrypt_list():
    encryption_dict = {'A': '1', 'B': '2', 'C': '3'}
    sde = SimpleDictionaryEncryption(encryption_dict)
    assert sde.decrypt(['1', '2', '3']) == "ABC"
    assert sde.decrypt(['1', '2', 'X']) == "AB'Invalid Input'"


def test_simple_dictionary_encryption_decrypt_str():
    encryption_dict = {'A': '1', 'B': '2', 'C': '3'}
    sde = SimpleDictionaryEncryption(encryption_dict)
    assert sde.decrypt("123") == NotImplemented


def test_validate_input():
    encryption_instance = SimpleDictionaryEncryption({})
    assert encryption_instance._validate_input("test") is None
    assert encryption_instance._validate_input(["test1", "test2"]) is None
    with pytest.raises(ValueError, match="Input must be a non-empty string or list"):
        encryption_instance._validate_input("")
    with pytest.raises(ValueError, match="Input must be a non-empty string or list"):
        encryption_instance._validate_input(None)
    with pytest.raises(ValueError, match="Input must be a non-empty string or list"):
        encryption_instance._validate_input(123)
    with pytest.raises(ValueError, match="Input must be a non-empty string or list"):
        encryption_instance._validate_input(123.45)