"""
Write a Python program to replace all occurrences of space, comma, or dot with a colon.

text = 'Python Exercises, PHP exercises.'

"""

import re


def replace(line):
    return re.sub(r"[\s,.]", ":", line)


def main():
    text = 'Python Exercises, PHP exercises.'
    print(replace(text))


main()
