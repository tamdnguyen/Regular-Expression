# Write a Python program to check for a number at the end of a string.
import re


def check(line):
    num = re.search(r"\d+$", line)
    if num:
        return True
    else:
        return False


def main():
    print(check('abcdef'))
    print(check('abcdef6'))


main()

'''
Model solution from w3resource.com

import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('abcdef'))
print(end_num('abcdef6'))

'''