"""
Write a Python program to search some literals strings in a string.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

"""

import re

"""
Using findall() and print

def search(line):
    word = re.findall(r"fox|dog|horse", line)
    return word


def main():
    line = 'The quick brown fox jumps over the lazy dog.'
    words = search(line)
    for word in words:
        print(word)
        
"""


def search(line):
    patterns = ["fox", "dog", "horse"]
    for pattern in patterns:
        print('Find "{:s}" in "{:s}": '.format(pattern, line))
        if re.search(pattern, line):
            print("Found")
        else:
            print("Not found")


def main():
    line = 'The quick brown fox jumps over the lazy dog.'
    search(line)


main()
