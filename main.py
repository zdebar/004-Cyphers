import logging
from abc import ABC, abstractmethod
from cyphers.NATO_alphabet import NATOPhoneticAlphabet
from gui.gui_terminal import intro_screen

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
CYPHER_LIST = [NATOPhoneticAlphabet, NATOPhoneticAlphabet]


if __name__ == "__main__":
    pass


