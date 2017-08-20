"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

# word_format = input("Enter '%' for a consonant and '#' for a vowel: ")
#
# word = ""
# for kind in word_format.lower():
#     if kind == "%":
#         word += random.choice(CONSONANTS)
#     elif kind == "#":
#         word += random.choice(VOWELS)
#     else:
#         word += kind
#
#
# print(str.title(word))

word = ""
random_word = random.randint(3,8)

for i in range(random_word):
    number = random.randint(0,100)
    if number >= 70:
        word += random.choice(VOWELS)
    else:
        word += random.choice(CONSONANTS)

print(str.title(word))