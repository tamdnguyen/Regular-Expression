"""
Write a Python program to match if two words from a list of words starting with letter 'P'.

# Sample strings.
words = ["Python PHP", "Java JavaScript", "c c++"]

MODEL SOLUTION (the question was somehow vague and caused obvious confusion)

import re

# Sample strings.
words = ["Python PHP", "Java JavaScript", "c c++"]

for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        # Check for success
        if m:
            print(m.groups())

"""

import re


def check_list(words):
    count = 0
    list_P = []
    for word in words:
        match = re.match(r"^P", word)
        if match:
            list_P.append(word)
            count += 1
    if count == 2:
        return True, list_P
    else:
        return False, list_P


def main():
    words = ["Python PHP", "Java JavaScript", "c c++", "peppa", "P?per"]
    list_match, list_P = check_list(words)
    if list_match:
        print("List {} is valid".format(words))
        print('The words starting with letter "P" are: ')
        for word in (list_P):
            if word != list_P[-1]:
                print(word, end=", ")
            else:
                print(word)
    else:
        print('List "{}" is invalid'.format(words))


main()

