def invert_dictionary(input_dict: dict):
    return {value: key for key, value in input_dict.items()}


def return_non_valid_characters(characters: str or list, test_dict: dict) -> set:
    non_valid_char = set()
    for char in characters:
        if (char != " ") and (char not in test_dict):
            non_valid_char.add(char)

    return non_valid_char





