# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re


def check_regex(line):
    yes = re.search(r"^[a-z]+?_[a-z]+$", line)
    if yes:
        return True
    else:
        return False


def main():
    print(check_regex("aab_cbbbc"))
    print(check_regex("aab_Abbbc"))
    print(check_regex("Aaab_abbbc"))


main()
