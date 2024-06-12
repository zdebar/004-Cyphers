import pytest
from cyphers.cypher_abstract import EncryptionMethod


def test_abstract_class_instantiation():
    with pytest.raises(TypeError):
        EncryptionMethod()
