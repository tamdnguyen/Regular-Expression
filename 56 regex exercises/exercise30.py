""""
Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

street = '21 Ramkrishna Road'

"""

import re


def abbreviate(line):
    return re.sub(r"Road", "Rd.", line)


def main():
    street = '21 Ramkrishna Road'
    print(abbreviate(street))


main()
