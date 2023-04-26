import math


class TranspositionCipher:
    @staticmethod
    def encrypt(text, key):
        cipher_text = [''] * key
        for col in range(key):
            position = col
            while position < len(text):
                cipher_text[col] += text[position]
                position += key
        return ''.join(cipher_text)

    @staticmethod
    def decrypt(cipher_text, key):
        num_columns = math.ceil(len(cipher_text) / key)
        num_rows = key
        num_shaded_boxes = (num_columns * num_rows) - len(cipher_text)

        plaintext = [''] * num_columns
        col = 0
        row = 0

        for symbol in cipher_text:
            plaintext[col] += symbol
            col += 1

            if (col == num_columns) or (col == num_columns - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(plaintext)
