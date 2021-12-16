# Write a Python program that matches a string that has an a followed by zero or more b's.

import re


def check_regex(line):
    yes = re.search(r"a(b*)", line)
    if yes:
        return True
    else:
        return False


def main():
    print(check_regex("a"))
    print(check_regex("ac"))
    print(check_regex("ab"))
    print(check_regex("abbc"))
    print(check_regex("cbd"))


main()
