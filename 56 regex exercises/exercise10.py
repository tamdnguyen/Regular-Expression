# Write a Python program that matches a word at the beginning of a string.

import re


def check_regex(line):
    yes = re.search(r"^\w+ ", line)
    if yes:
        return True
    else:
        return False


def main():
    print(check_regex("The quick brown fox jumps over the lazy dog."))
    print(check_regex(" The quick brown fox jumps over the lazy dog."))


main()