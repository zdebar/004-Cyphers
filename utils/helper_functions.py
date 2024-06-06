def invert_dictionary(input_dict: dict) -> dict:
    inverted_dict = {}
    for key, value in input_dict.items():

        if not isinstance(value, (int, float, str, tuple, frozenset, bytes)):
            raise TypeError(f"Unhashable value '{value}' of type '{type(value).__name__}' cannot be used as a key.")

        if value in inverted_dict:
            raise ValueError(
                f"Duplicate value found for keys '{inverted_dict[value]}' and '{key}' with value '{value}'")

        inverted_dict[value] = key

    return inverted_dict
