"""
Write a Python program to remove words from a string of length between 1 and a given number.

text = "The quick brown fox jumps over the lazy dog."

remove words with length between 1 and 3
expected output: quick brown jumps over lazy.
"""

import re


def remove(line):
    """
    with \W:  quick brown jumps over lazy.
    without \W:  quick brown  jumps over  lazy . There are multiple whitespace, so that \W helps delete them.

    """
    word = re.compile(r"\W\b\w{1,3}\b")
    return word.sub("", line)


def main():
    text = "The quick brown fox jumps over the lazy dog."
    print(remove(text))


main()
