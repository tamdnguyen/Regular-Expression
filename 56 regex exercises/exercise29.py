"""
Write a Python program to separate and print the numbers and their position of a given string.

text = "The following example creates an ArrayList with a capacity of 50 elements.
Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
"""

import re


def separate(line):
    pattern = r"[0-9]+"
    if not re.search(pattern, line):
        print("No number found")
        return 1
    else:
        for i in re.finditer(pattern, line):
            pos = i.span()
            print("Found number {:d} position from character {:d} to {:d}".
                  format(int(i.group()), int(pos[0]), int(pos[1])))


def main():
    text = "10The following example creates an ArrayList with a capacity of 50 elements. " \
           "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    separate(text)


main()