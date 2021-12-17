# Write a Python program to remove leading zeros from an IP address.

import re


def remove(line):
    pattern = r"\.0+"
    removed = re.sub(pattern, ".", line)
    return removed


def main():
    print(remove("216.08.094.196"))


main()
