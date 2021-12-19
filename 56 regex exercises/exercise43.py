"""
Write a Python program to split a string at uppercase letters.

"""

import re


def split(line):
    return re.findall(r"[A-Z][^A-Z]*", line)


def main():
    text = "PythonTutorialAndExercises"
    print(split(text))


main()
