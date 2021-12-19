"""
Write a Python program to remove everything except alphanumeric characters from a string.

text1 = '**//Python Exercises// - 12. '

"""

import re


def remove(line):
    pattern = r"[^a-zA-Z0-9]"
    return re.sub(pattern, "",line)


def main():
    text1 = '**//Python Exercises// - 12. '
    print(remove(text1))


main()
