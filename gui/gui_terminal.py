import logging

from cyphers.NATO_alphabet import NATOPhoneticAlphabet
from cyphers.cypher_abstract import EncryptionMethod
from cyphers.Morse_code import MorseCode
from cyphers.Caesar_cypher import CaesarCypher

CYPHER_LIST = [NATOPhoneticAlphabet, MorseCode, CaesarCypher]

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def intro_screen():
    print(f"\nWelcome to CYPHER UTILITY.\n")


def select_cypher_from_menu(my_list: list):

    while True:
        for index, item in enumerate(my_list, 1):
            print(f"{index:>2}. {item.name}")
        chosen_cypher = int(input(f"\nSelect encryption method [1 to {len(my_list)}]: "))
        if chosen_cypher in range(1, len(CYPHER_LIST) + 1):
            break
        else:
            print("\nInvalid Input. Try again.")

    return my_list[chosen_cypher-1]


def select_cypher_or_decypher(strategy: EncryptionMethod):

    print(f"\nSelected encryption method: {strategy.name}")

    while True:
        option = input(f"Choose between encryption or decryption [e or d]: ")
        if option.upper() == "E":
            return strategy.encrypt
        if option.upper() == "D":
            return strategy.decrypt
        print("\nInvalid Input. Try again.")


def run_encryption(method: EncryptionMethod.encrypt or EncryptionMethod.decrypt):

    while True:
        try:
            to_encrypt = input(f"\nWrite message to encrypt / encrypt: ")
            processed = method(to_encrypt)
            logging.debug(processed)
            print(f"Encrypted message: {processed}")
        except Exception as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":
    intro_screen()
    selected_method = select_cypher_from_menu(CYPHER_LIST)
    strategy_2 = selected_method()
    selected_strategy = select_cypher_or_decypher(strategy_2)
    run_encryption(selected_strategy)
