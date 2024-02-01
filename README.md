# LAB - Class 18

## Project: Cryptography - Caesar Cipher

- *Version: 1.0*

### Author: Ekow Yawson

**Project Overview**:

This project implements a **Caesar Cipher** encryption and decryption tool in Python. The tool provides functions to encrypt a message by shifting its letters a certain number of places in the alphabet, decrypt a message by shifting the letters back, and even crack an encrypted message without prior knowledge of the shift.

This tool is designed to demonstrate basic cryptographic principles and should not be used for securing sensitive information.

### Features

1. **`encrypt(phrase, shift)`**: Encrypts a given phrase by shifting its letters by a specified number. Non-alphabetical characters are left unchanged.

2. **`decrypt(encrypted_text, shift)`**: Decrypts a given piece of encrypted text by shifting its letters back by the specified number.

3. **`crack(encrypted_text)`**: Attempts to crack an encrypted text by trying all possible shifts and selecting the one with the highest number of recognizable English words. It returns the decrypted text and the shift used.

4. **Corpus Utilization**: Utilizes a simple corpus of common English words to help identify the most likely shift used in encryption.

5. **Non-Alpha Character Handling**: The encryption process allows non-alpha characters but ignores them, including white space, during the encryption and decryption processes.

### Setup

**Environment Setup Steps**:

1. Clone the repository to your local machine.
2. No external libraries are specifically required for this project; however, `pytest` is used for the testing suite
3. To install the required libraries/modules, run the following command:
   - `pip install -r requirements.txt`.
4. To use the modules, you may chose to create a `main.py` and import the desired functions:
   - `from caesar_cipher.cipher import encrypt, decrypt, crack`

### How to Run the Application

To use the encryption or decryption functions, call them with the appropriate parameters from your Python environment.

**Example**:

```python
phrase = "Hello, World!"
shift = 5

# Encrypt the phrase
encrypted_phrase = encrypt(phrase, shift)
print(f"Encrypted: {encrypted_phrase}")

# Decrypt the phrase
decrypted_phrase = decrypt(encrypted_phrase, shift)
print(f"Decrypted: {decrypted_phrase}")

# Assuming `encrypted_phrase` is an encrypted text with an unknown shift
cracked_phrase, used_shift = crack(encrypted_phrase)
print(f"Cracked Phrase: {cracked_phrase}")
print(f"Used Shift: {used_shift}")
```

### Links and Resources

- [Encryption, Decryption & Hacking](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/encryption-decryption-and-code-cracking)
- [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Cryptography Crash Course](https://www.youtube.com/watch?v=jhXCTbFnK8o)
- [Introduction to Cryptography](https://thebestvpn.com/cryptography/)
- [How Computers Generate Random Numbers](https://www.howtogeek.com/183051/htg-explains-how-computers-generate-random-numbers/)

### Tests

Tests are provided in the `tests` directory. To run the tests, create an virtual environment with **venv** at the root of the project and run pytest:

**Example**:

```python
python3 -m venv .venv
source .venv/bin/activate
pytest
```

### Contributors

- Stephanie G Johnson
- Latherio Kidd
