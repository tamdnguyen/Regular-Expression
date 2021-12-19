"""
Write a Python program to remove multiple spaces in a string.

"""

import re


def remove(line):
    pattern = r"\s{2,}"
    return re.sub(pattern, " ", line)


def main():
    text1 = 'Python      Exercises'
    print(remove(text1))


main()
