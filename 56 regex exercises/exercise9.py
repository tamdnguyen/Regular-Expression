# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re


def check_regex(line):
    yes = re.search(r"a.*?b$", line)
    if yes:
        return True
    else:
        return False


def main():
    print(check_regex("aabbbbd"))
    print(check_regex("aabAbbbc"))
    print(check_regex("accddbbjjjb"))


main()