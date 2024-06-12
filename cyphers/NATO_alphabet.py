import logging
from cyphers.Simple_Dictionary_Cypher import SimpleDictionaryEncryption

ENCRYPTION_TEST_STR = "postman"
DECRYPTION_TEST_LIST = ['Papa', 'Oscar', 'Sierra', 'Tango', 'Mike', 'Alpha', 'November']

NATO_ALPHABET = {
    'A': 'Alpha',   'B': 'Bravo',    'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo',    'F': 'Foxtrot',  'G': 'Golf',    'H': 'Hotel',
    'I': 'India',   'J': 'Juliett',  'K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',    'N': 'November', 'O': 'Oscar',   'P': 'Papa',
    'Q': 'Quebec',  'R': 'Romeo',    'S': 'Sierra',  'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor',   'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'
}


class NATOPhoneticAlphabet(SimpleDictionaryEncryption):

    name = "NATO phonetical alphabet"

    def __init__(self):
        super().__init__(NATO_ALPHABET)

    def decrypt(self, input_text: list) -> str:
        logging.debug(f"Input to encrypt: {input_text}")
        return "".join(self.decryption_key.get(char.upper(), char) for char in input_text if char != " ")


if __name__ == "__main__":
    cypher = NATOPhoneticAlphabet()
    print(cypher.encrypt(ENCRYPTION_TEST_STR))
    print(cypher.decrypt(DECRYPTION_TEST_LIST))

