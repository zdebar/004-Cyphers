def invert_dictionary(input_dict: dict) -> dict:
    """
    Inverts dictionary to value: key for decryption.
    """
    inverted_dict = {}
    for key, value in input_dict.items():

        # Checks if dict.value is hashable
        if not isinstance(value, (int, float, str, tuple, frozenset, bytes)):
            raise TypeError(f"Unhashable value '{value}' of type '{type(value).__name__}' cannot be used as a key.")

        # Checks if dict.value is duplicate
        if value in inverted_dict:
            raise ValueError(
                f"Duplicate value found for keys '{inverted_dict[value]}' and '{key}' with value '{value}'")
        inverted_dict[value.upper()] = key

    return inverted_dict


def print_invalid_input():
    print("\nInvalid Input. Try again.\n")


def ask_for_character_shift():
    while True:
        try:
            shift = int(input(f"\nEnter character shift [integer]: "))
            break
        except ValueError:
            print_invalid_input()
    return shift
