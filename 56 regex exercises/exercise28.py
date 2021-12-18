"""
Write a Python program to find all words starting with 'a' or 'e' in a given string.

# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

"""

import re


def find(line):
    words = re.findall(r"\b[ae]\w+", line, flags=re.IGNORECASE)
    return words


def main():
    text = "The following example creates an ArrayList with a capacity of 50 elements. " \
           "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    text2 = "Enter here we have an amazing Apple store. All the edges are excellent"
    print(find(text))
    print(find(text2))


main()


