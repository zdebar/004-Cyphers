import logging
from cyphers.NATO_alphabet import NATOPhoneticAlphabet
from cyphers.Morse_code import MorseCode
from cyphers.Caesar_cypher import CaesarCypher
from controller.controller import run_cypher_utility

CYPHER_LIST = [NATOPhoneticAlphabet, MorseCode, CaesarCypher]

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    run_cypher_utility(CYPHER_LIST)


