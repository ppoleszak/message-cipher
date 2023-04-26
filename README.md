# Message Cipher Encryptor & Decryptor

This message encryptor and decryptor combines a simplified Homophonic Cipher with a Transposition Cipher to provide a more secure
encryption method.

## How it works

The program consists of several classes:

1. `TranspositionCipher` - Encrypts and decrypts text using the transposition cipher.
2. `HomophonicCipher` - Encrypts and decrypts text using a simplified homophonic cipher, without numeric
   substitutions.
3. `MessageEncryptor` - Combines the two ciphers to encrypt and decrypt messages.

### TranspositionCipher

The `TranspositionCipher` class provides the following methods:

* `encrypt(text, key)`: Encrypts the given text using the specified key.
* `decrypt(cipher_text, key)`: Decrypts the given cipher text using the specified key.

### HomophonicCipher

The \`HomophonicCipher\` class provides the following methods:

* `encrypt_character(char)`: Encrypts the given character using the homophonic substitution table.
* `decrypt_character(char, index)`: Decrypts the given character using the homophonic substitution table and index.

### MessageEncryptor

The `MessageEncryptor` class provides the following methods:

* `encrypt(message_param)`: Encrypts the given message using the combined Homophonic and Transposition Ciphers.
* `decrypt(encrypted_message_param)`: Decrypts the given encrypted message using the combined Homophonic and
  Transposition Ciphers.

## Usage

Create an instance of the \`MessageEncryptor\` class, providing column and row keys:

```python
encryptor = MessageEncryptor(column_key, row_key)
```

Then, you can use the \`encrypt\` and \`decrypt\` methods to encrypt and decrypt messages:

```python
encrypted_message = encryptor.encrypt(message)
decrypted_message = encryptor.decrypt(encrypted_message)
```
