"""
Write a Python program to find the substrings within a string.

Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'

Note: There are two instances of exercises in the input string.

"""

import re


def find(line):
    pattern = "exercises"
    matches = re.findall(pattern, line)
    for match in matches:
        print('Found "{:s}" in the given string.'.format(pattern))


def main():
    find('Python exercises, PHP exercises, C# exercises')


main()
