# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re


def check_regex(line):
    yes = re.search(r"[A-Z]+[a-z]+$", line)
    if yes:
        return True
    else:
        return False


def main():
    print(check_regex("AaBbGg"))
    print(check_regex("Python"))
    print(check_regex("python"))
    print(check_regex("PYTHON"))
    print(check_regex("aA"))
    print(check_regex("Aa"))


main()
