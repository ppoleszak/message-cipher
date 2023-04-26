from encryptor.message_encryptor import MessageEncryptor

if __name__ == '__main__':
    input_message = "Funny Cipher!"
    input_column_key = 5
    input_row_key = 7

    encryptor = MessageEncryptor(input_column_key, input_row_key)
    encrypted_output = encryptor.encrypt(input_message)
    print(f'Encrypted message: {encrypted_output}')
    decrypted_output = encryptor.decrypt(encrypted_output)
    print(f'Decrypted message: {decrypted_output}')
