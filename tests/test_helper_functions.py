import pytest
from utils.helper_functions import invert_dictionary


NATO_ALPHABET = {
    'A': 'Alpha',   'B': 'Bravo',    'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo',    'F': 'Foxtrot',  'G': 'Golf',    'H': 'Hotel',
    'I': 'India',   'J': 'Juliett',  'K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',    'N': 'November', 'O': 'Oscar',   'P': 'Papa',
    'Q': 'Quebec',  'R': 'Romeo',    'S': 'Sierra',  'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor',   'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'
}


def test_invert_dictionary_empty():
    assert invert_dictionary({}) == {}


def test_invert_dictionary_duplicates():
    input_dict = {'x': 5, 'y': 5, 'z': 7}
    with pytest.raises(ValueError, match="Duplicate value found for keys 'x' and 'y' with value '5'"):
        invert_dictionary(input_dict)


def test_invert_dictionary_with_unhashable_values():
    input_dict = {'a': [1, 2], 'b': {3: 4}}
    with pytest.raises(TypeError, match="Unhashable value '\\[1, 2\\]' of type 'list' cannot be used as a key."):
        invert_dictionary(input_dict)
