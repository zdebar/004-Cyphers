import pytest
from cyphers.NATO_alphabet import NATOPhoneticAlphabet

ENCRYPTION_TEST_STR = "postman"
DECRYPTION_TEST_LIST = ['Papa', 'Oscar', 'Sierra', 'Tango', 'Mike', 'Alpha', 'November']


def test_encrypt():
    cypher = NATOPhoneticAlphabet()
    assert cypher.encrypt(ENCRYPTION_TEST_STR) == DECRYPTION_TEST_LIST
    assert cypher.encrypt(list(ENCRYPTION_TEST_STR)) == DECRYPTION_TEST_LIST
    assert cypher.encrypt("MONKEY") == ['Mike', 'Oscar', 'November', 'Kilo', 'Echo', 'Yankee']
    assert cypher.encrypt([]) == []
    assert cypher.encrypt("") == []


def test_decrypt():
    cypher = NATOPhoneticAlphabet()
    assert cypher.decrypt(DECRYPTION_TEST_LIST) == ENCRYPTION_TEST_STR.upper()
    assert cypher.decrypt("PapaOscar") == NotImplemented
