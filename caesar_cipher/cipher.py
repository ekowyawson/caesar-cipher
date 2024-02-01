import string

def encrypt(phrase, shift):
    """Encrypts a given phrase by shifting its letters by a specified number.

    Parameters:
        - `phrase` (str): The input string to be encrypted.
        - `shift` (int): The number of positions each letter in the phrase will be shifted.

    Returns:
        - `str`: The encrypted phrase, with non-alphabetical characters left unchanged.
    """
    encrypted = []
    for char in phrase:
        if char.isalpha():
            shifted_char = shift_char(char, shift)
            encrypted.append(shifted_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)


def decrypt(encrypted_text, shift):
    """Decrypts a given encrypted text by shifting its letters back by the specified number.

    Parameters:
        - `encrypted_text` (str): The encrypted text to be decrypted.
        - `shift` (int): The number of positions each letter in the encrypted text will be shifted back.

    Returns:
        - `str`: The decrypted text, with non-alphabetical characters left unchanged.
    """
    return encrypt(encrypted_text, -shift)


def shift_char(char, shift):
    """Shifts a single character by a specified number of positions, wrapping around the alphabet.

    Parameters:
        - `char` (str): The single character to be shifted.
        - `shift` (int): The number of positions to shift the character.

    Returns:
        - `str`: The shifted character.
    """
    if char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

# Going hard for this one...
# If a simple corpus of common English words is defined
english_words = ["the", "of", "and", "to", "a", "in", "that",
                 "it", "is", "was","he", "for", "with", "as",
                 "his", "on", "be", "at", "by", "not"]


def is_english_word(word):
    """Checks if a word exists in the defined corpus above.

    Parameters:
        - `word` (str): The word to check.

    Returns:
        - `bool`: True if the word exists in the corpus, False otherwise.
    """
    return word.lower() in english_words


def count_english_words(text):
    """Counts how many words in a text exist in the predefined corpus.

    Parameters:
        - `text` (str): The text whose words are to be checked against the corpus.

    Returns:
        - `int`: The number of words in the text that exist in the English corpus.
    """
    words = text.split()
    sum_words = sum(is_english_word(word.strip(string.punctuation)) for word in words)
    return sum_words


def crack(encrypted_text):
    """Attempts to crack an encrypted text by trying all possible shifts and
    selecting the one with the highest number of recognizable English words.

    Parameters:
        - `encrypted_text` (str): The text to be cracked.

    Returns:
        - `tuple`: A tuple containing the decrypted text and the shift used, or an empty string if
             unable to confidently decrypt.
    """
    best_shift = 0
    max_english_words = 0
    for shift in range(26):
        decrypted_attempt = decrypt(encrypted_text, shift)
        english_word_count = count_english_words(decrypted_attempt)
        if english_word_count > max_english_words:
            max_english_words = english_word_count
            best_shift = shift

    # At least 50% of the words must be recognized as words
    threshold_percentage = 0.5
    words_in_attempt = len(encrypted_text.split())
    if max_english_words / words_in_attempt >= threshold_percentage:
        return decrypt(encrypted_text, best_shift), best_shift
    else:
        return ""
