"""
Write a Python program to find all adverbs and their positions in a given sentence. Go to the editor

Sample text : "Clearly, he has no excuse for such behavior."

"""

import re


def find_adv(line):
    pattern = r"[a-zA-Z]+?ly"
    for i in re.finditer(pattern, line):
        print('Found adverb "{:s}" from character {:d} to {:d}'.format(i.group(), i.start(), i.end()))


def main():
    text = "Clearly, he has no excuse for ugly desperately beautifully behavior."
    find_adv(text)


main()
