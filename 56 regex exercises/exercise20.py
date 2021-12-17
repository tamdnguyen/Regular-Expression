"""
Write a Python program to search a literals string in a string and also find the location within
the original string where the pattern occurs.

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

"""


import re


def search(line):
    literal = "fox"
    match = re.search(literal, line)
    if match:
        print('Found literals string "{:s}" in "{:s}"!'.format(literal, line))
        print("Location: start from position {:d} to {:d} (First letter is position 0).".format(match.start(), match.end()))


def main():
    line = 'The quick brown fox jumps over the lazy dog.'
    search(line)


main()


