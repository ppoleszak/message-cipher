from ciphers.homophobic_cipher import HomophonicCipher
from ciphers.transposition_cipher import TranspositionCipher


class MessageEncryptor:
    def __init__(self, column_key_param, row_key_param):
        self.homophonic_cipher = HomophonicCipher()
        self.transposition_cipher = TranspositionCipher()
        self.column_key = column_key_param
        self.row_key = row_key_param
        self.separator = '\x00'
        self.group_size = 4

    def encrypt(self, message_param):
        encrypted_chars_with_indices = [self.homophonic_cipher.encrypt_character(char) for char in message_param]
        encrypted_text = ''.join(char for char, _ in encrypted_chars_with_indices)
        indices = ''.join(str(index).zfill(2) for _, index in encrypted_chars_with_indices)

        combined_text = encrypted_text + self.separator + indices
        encrypted_text = self.transposition_cipher.encrypt(combined_text, self.column_key)
        encrypted_text = self.transposition_cipher.encrypt(encrypted_text, self.row_key)

        return encrypted_text

    def decrypt(self, encrypted_message_param):
        decrypted_text = self.transposition_cipher.decrypt(encrypted_message_param, self.row_key)
        decrypted_text = self.transposition_cipher.decrypt(decrypted_text, self.column_key)

        decrypted_text_parts = decrypted_text.split(self.separator)
        encrypted_text, encrypted_indices = decrypted_text_parts

        decrypted_chars = []
        index_counter = 0

        for char in encrypted_text:
            index_str = encrypted_indices[index_counter:index_counter + 2]
            index = int(index_str) - 1 if index_str.isdigit() else -1
            index_counter += 2
            decrypted_chars.append(self.homophonic_cipher.decrypt_character(char, index))

        return ''.join(decrypted_chars)
