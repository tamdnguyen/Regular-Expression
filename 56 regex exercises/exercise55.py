"""
Write a Python program to convert a given string to snake case.

Use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+".
Use re.sub() to match all words in the string, str.lower() to lowercase them.
Finally, use str.join() to combine all word using - as the separator.

Input:
print(snake_case('JavaScript'))
print(snake_case('GDScript'))
print(snake_case('BTW...what *do* you call that naming style? snake_case? '))

Sample Output:
java-script
gd-script
btw...-what-*-do*-you-call-that-naming-style?-snake-case?

"""

import re


def snake_case(line):
    replace_space = re.sub(r"(_|-)+", " ", line)
    words = re.findall(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+", replace_space)
    return words


def main():
    print(snake_case('JavaScript'))
    print(snake_case('GDScript'))
    print(snake_case('BTW...what *do* you call that naming style? snake_case? '))


main()
