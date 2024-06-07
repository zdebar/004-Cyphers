import logging

from cyphers.NATO_alphabet import NATOPhoneticAlphabet
from cyphers.cypher_abstract import EncryptionMethod
from cyphers.Morse_code import MorseCode
from cyphers.Caesar_cypher import CaesarCypher

CYPHER_LIST = [NATOPhoneticAlphabet, MorseCode, CaesarCypher]

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def run_cypher_utility():
    print(f"\nWelcome to CYPHER UTILITY.\n")
    select_cypher_from_menu(CYPHER_LIST)


def select_cypher_from_menu(my_list: list):

    while True:
        for index, item in enumerate(my_list, 1):
            print(f"{index:>2}. {item.name}")
        try:
            chosen_cypher = input(f"\nSelect encryption method [1 to {len(my_list)}, 'exit']: ")
            if chosen_cypher.upper() == "EXIT":
                break
            strategy = my_list[int(chosen_cypher) - 1]
            select_cypher_or_decypher(strategy)
        except IndexError:
            print("\nInvalid Input. Try again.\n")
        except ValueError:
            print("\nInvalid Input. Try again.\n")


def select_cypher_or_decypher(strategy: EncryptionMethod):

    print(f"\nSelected encryption method: {strategy.name}")

    while True:
        option = input(f"Choose between encryption or decryption [E or D]: ")
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


def validate_input(input_str):
    pass


if __name__ == "__main__":
    run_cypher_utility()

