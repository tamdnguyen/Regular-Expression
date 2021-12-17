# Write a Python program where a string will start with a specific number.

import re


def match(line):
    text = re.compile(r"^5")
    if text.match(line):
        return True
    else:
        return False


def main():
    print(match('5-2345861'))
    print(match('6-2345861'))
    print(match("5656582394823"))


main()