from cyphers.cypher_abstract import EncryptionMethod
from utils.helper_functions import print_invalid_input
import logging


def welcome_screen() -> None:
    print("\nWelcome to Cypher Utility.\n")


def select_cypher_from_menu(cypher_list: list):

    while True:
        for index, item in enumerate(cypher_list, 1):
            print(f"{index:>2}. {item.name}")
        try:
            chosen_cypher = input(f"\nSelect encryption method [1 to {len(cypher_list)}]: ")
            strategy = cypher_list[int(chosen_cypher) - 1]
            return strategy
        except IndexError or ValueError:
            print_invalid_input()


def select_cypher_or_decypher(strategy: EncryptionMethod):

    print(f"\nSelected encryption method: {strategy.name}\n")

    while True:
        option = input(f"Choose between encryption or decryption ['E' or 'D']: ")
        if option.upper() == "E":
            return strategy.encrypt
        if option.upper() == "D":
            return strategy.decrypt
        print_invalid_input()


def ask_for_input():
    return input(f"\nWrite message to encrypt / encrypt: ")


def run_encryption(method: EncryptionMethod.encrypt or EncryptionMethod.decrypt, ):

    while True:
        try:
            to_encrypt = input(f"\nWrite message to encrypt / decrypt: ")
            processed = method(to_encrypt)
            logging.debug(processed)
            print(f"\nEncrypted message: {processed}")
        except ValueError:
            print_invalid_input()


def run_cypher_utility(cypher_list):
    welcome_screen()
    strategy = select_cypher_from_menu(cypher_list)
    strategy_option = select_cypher_or_decypher(strategy())
    run_encryption(strategy_option)
