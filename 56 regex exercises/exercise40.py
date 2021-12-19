"""
Write a Python program to remove all whitespaces from a string.

"""

import re


def remove(line):
    pattern = r"\s"
    return re.sub(pattern, "", line)


def main():
    text1 = 'Python      Exercises'
    print(remove(text1))


main()