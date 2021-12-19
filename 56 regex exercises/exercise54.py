"""
Write a Python program to concatenate the consecutive numbers in a given string. Go to the editor
Original string:
Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready.
After concatenating the consecutive numbers in the said string:
Enter at 120 Kearny Street. The security desk can direct you to floor 16. Please have your identification ready.

"""

import re


def concatenate(line):
    num_space = re.compile(r"([0-9]+)(\s)([0-9]+.)")
    return num_space.sub(r"\1\3", line)


def main():
    text = "Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. " \
           "Please have your identification ready."
    print(concatenate(text))


main()
