"""
Write a Python program to find the occurrence and position of the substrings within a string.
Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'

"""

import re


def find(line):
    pattern = "exercises"
    if not re.search(pattern, line):
        print("Not found.")
        return 1
    else:
        for i in re.finditer(pattern, line):
            # get the position using .span(), from start() to end()
            pos = i.span()
            print('Substring "{:s}" found in "{:s}", location from character {:d} to {:d}.'.
                  format(pattern, line, int(pos[0]), int(pos[1])))


def main():
    find('Python exercises, PHP exercises, C# exercises')
    find("No exercise today for the students.")


main()
