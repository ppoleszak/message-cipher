import random


class HomophonicCipher:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.homophonic_substitutions = {
            char: [char, char.lower()]
            for index, char in enumerate(self.alphabet)
        }

    def encrypt_character(self, char):
        if char.upper() in self.homophonic_substitutions:
            substitution = random.choice(self.homophonic_substitutions[char.upper()])
            return substitution, self.homophonic_substitutions[char.upper()].index(substitution)
        return char, -1

    def decrypt_character(self, char, index):
        if index >= 0:
            for key, values in self.homophonic_substitutions.items():
                if char in values:
                    return key
        return char
