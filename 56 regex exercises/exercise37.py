"""
Write a python program to convert snake case string to camel case string.

"""

import re


def snake_to_camel(line):
    """
    if the first word in the string only has 1 character before the _ then not capitalize that character
    if there are more than 1, capitalize the first character of the first world
    for e.g., python_exercise -> PythonExercise, but i_phone -> iPhone
    """
    pattern = r"(.+)_(\w)(\w+)"
    match = re.search(pattern, line)
    if match:
        if len(match.group(1)) == 1:
            capital_char = match.group(2)
            return match.group(1) + capital_char.upper() + match.group(3)
        else:
            first_capital = match.group(1)[0]
            first_word_left = match.group(1)[1:]
            second_capital = match.group(2)
            return first_capital.upper() + first_word_left + second_capital.upper() + match.group(3)
    else:
        return "Invalid string. Not in snake case format."


def main():
    print(snake_to_camel('python_exercises'))
    print(snake_to_camel("i_phone"))
    print(snake_to_camel("eBay"))
    print(snake_to_camel("tam_nguyen"))
    print(snake_to_camel("e_bay"))


main()
