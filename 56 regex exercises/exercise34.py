"""
Write a Python program to find all three, four, five characters long words in a string.

text = 'The quick brown fox jumps over the lazy dog.'

"""

import re


def find(line):
    words = re.findall(r"\b\w{3,5}\b", line)
    return words


def main():
    text = 'The quick brown fox jumps over the lazy dog.'
    print(find(text))


main()