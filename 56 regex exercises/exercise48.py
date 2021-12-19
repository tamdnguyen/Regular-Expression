"""
Write a Python program to check a decimal with a precision of 2.

"""

import re


def check_precision(line):
    decimal = re.compile(r"^[0-9]+(\.[0-9]{1,2})?$") # here, the ? is for check if .ab exists or not
    precision = decimal.search(line)
    if precision:
        return True
    else:
        return False


def main():
    print(check_precision('123.11'))
    print(check_precision('123.1'))
    print(check_precision('123'))
    print(check_precision('0.21'))

    print(check_precision('123.1214'))
    print(check_precision('3.124587'))
    print(check_precision('e666.86'))


main()
