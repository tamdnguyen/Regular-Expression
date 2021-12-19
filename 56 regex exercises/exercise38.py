"""
Write a Python program to extract values between quotation marks of a string.

"""

import re


def extract(line):
    pattern = r'"(.*?)"'
    match = re.findall(pattern, line)
    print(match)


def main():
    text1 = '"Python", "PHP", "Java"'
    extract(text1)


main()
