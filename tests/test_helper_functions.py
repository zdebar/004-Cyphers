import pytest
from utils.helper_functions import invert_dictionary, return_non_valid_characters, all_upper


NATO_ALPHABET = {
    'A': 'Alpha',   'B': 'Bravo',    'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo',    'F': 'Foxtrot',  'G': 'Golf',    'H': 'Hotel',
    'I': 'India',   'J': 'Juliett',  'K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',    'N': 'November', 'O': 'Oscar',   'P': 'Papa',
    'Q': 'Quebec',  'R': 'Romeo',    'S': 'Sierra',  'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor',   'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'
}


@all_upper
def decorator_example(x):
    return x


def test_invert_dictionary():
    assert invert_dictionary({}) == {}


def test_return_non_valid_characters():
    assert return_non_valid_characters("BASIC VALID INPUT", NATO_ALPHABET) == set()
    assert return_non_valid_characters("Aaá", NATO_ALPHABET) == {"a", "á"}


def test_decorator():
    assert decorator_example("lets try some optionS") == "LETS TRY SOME OPTIONS"
    assert decorator_example(["a", "b"]) == (["A", "B"])
