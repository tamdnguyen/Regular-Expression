# Write a Python program that matches a string that has an a followed by two to three 'b'.

# Write a Python program that matches a string that has an a followed by zero or one 'b'.

import re


def check_regex(line):
    yes = re.search(r"ab{2,3}", line)
    if yes:
        return True
    else:
        return False


def main():
    print(check_regex("a"))
    print(check_regex("aabbc"))
    print(check_regex("ab"))
    print(check_regex("aabbbbbc"))
    print(check_regex("cbd"))


main()
