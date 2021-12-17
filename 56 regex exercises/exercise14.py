# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re


def check_regex(line):
    yes = re.search(r"[^a-zA-Z0-9_]", line)
    if yes:
        return False
    else:
        return True


def main():
    print(check_regex("The quick brown fox jumps over the lazy dog."))
    print(check_regex("Python_Exercises_1"))


main()