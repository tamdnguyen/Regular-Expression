"""
Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

"Exercises number 1, 12, 13, and 345 are important"

"""

import re


def search(line):
    nums = re.findall(r"[0-9]{1,3}", line)
    return nums


def main():
    line = "Exercises number 1, 12, 13, and 345 are important"
    nums = search(line)
    print('In the string "{:s}", numbers are:'.format(line))
    for num in nums:
        print(num)


main()