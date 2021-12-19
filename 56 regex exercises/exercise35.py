"""
Write a Python program to find all words which are at least 4 characters long in a string.

"""

import re


def find(line):
    words = re.findall(r"\b\w{4,}\b", line)
    return words


def main():
    text = 'The quick brown fox jumps over the lazy dog.'
    print(find(text))


main()
