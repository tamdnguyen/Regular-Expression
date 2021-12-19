"""
Write a python program to convert camel case string to snake case string.

print(camel_to_snake('PythonExercises'))

"""

import re


def camel_to_snake(line):
    pattern = r"(.)([A-Z]\w+)"
    return re.sub(pattern, r"\1_\2", line).lower()


def main():
    print(camel_to_snake('PythonExercises'))
    print(camel_to_snake("iPhone"))


main()
