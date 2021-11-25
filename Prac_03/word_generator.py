"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = input("Enter the word format: ").lower()
    while not is_valid_format(word_format):
        print("Invalid format")
        word_format = input("Enter the word format: ").lower()
    word = ""
    for kind in word_format:
        if kind == "%":
            word += random.choice(CONSONANTS)
        elif kind == "#":
            word += random.choice(VOWELS)
        else:
            word += kind
    print(word)


def is_valid_format(word_format):
    for character in word_format:
        if character != 'c' and character != 'v':
            return False
    return True


main()
