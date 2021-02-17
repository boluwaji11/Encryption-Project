import random


class CodeGenerator:
    def __init__(self):
        # Using ASCII characters as the code for encryption
        self.__FIRST_ASCII = 33
        self.__LAST_ASCII = 126
        # Create empty dictionary to hold the encryption codes
        self.__encryption_codes = {}

    def generate_code(self):

        code_values = list(range(self.__FIRST_ASCII, self.__LAST_ASCII + 1))

        # Randomize the list of code values
        code_values = random.sample(code_values, len(code_values))

        for i in range(len(code_values)):
            self.__encryption_codes[chr(i + self.__FIRST_ASCII)] = chr(code_values[i])

        # Return dictionary of encryption code

    def get_code(self):
        return self.__encryption_codes