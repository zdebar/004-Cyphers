import logging
from cyphers.NATO_alphabet import NATOPhoneticAlphabet
from cyphers.Morse_code import MorseCode
from cyphers.Caesar_cypher import CaesarCypher
from gui.gui_terminal import run_cypher_utility, select_cypher_from_menu, select_cypher_or_decypher, run_encryption

CYPHER_LIST = [NATOPhoneticAlphabet, MorseCode, CaesarCypher]

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    run_cypher_utility()
    selected_method = select_cypher_from_menu(CYPHER_LIST)
    strategy_2 = selected_method()
    selected_strategy = select_cypher_or_decypher(strategy_2)
    run_encryption(selected_strategy)


