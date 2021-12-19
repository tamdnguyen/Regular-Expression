"""
Write a Python program to remove the ANSI escape sequences from a string.

text = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"

"""

import re


def find_sequence(line):
    ansi_escape = re.compile(r"\x1b[^m]*m")
    return ansi_escape.sub("", line)


def main():
    text = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
    print(text)
    print(find_sequence(text))


main()
