"""
Write a Python program to split a string with multiple delimiters.

Note : A delimiter is a sequence of one or more characters used to specify the boundary between separate,
independent regions in plain text or other data streams. An example of a delimiter is the comma character,
which acts as a field delimiter in a sequence of comma-separated values.

text = 'The quick brown\nfox jumps*over the lazy dog.'

"""

import re


def split(line):
    delimiter = r"[,;\"\'{}\|\/]"
    return re.split(r"[,;\"\'{}\|\/\n*]", line)


def main():
    text = 'The quick brown\nfox jumps*over the lazy dog.'
    print(split(text))


main()
