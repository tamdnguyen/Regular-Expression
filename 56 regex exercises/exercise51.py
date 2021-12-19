"""
Write a Python program to insert spaces between words starting with capital letters.

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

Sample Output:

Python
Python Exercises
Python Exercises Practice Solution

MODEL SOLUTION
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))


"""

import re


def capital_words_spaces(line):
    capital = re.compile(r"(\w)([A-Z])")
    words = capital.sub(r"\1 \2", line)
    return words


def main():
    print(capital_words_spaces("Python"))
    print(capital_words_spaces("PythonExercises"))
    print(capital_words_spaces("PythonExercisesPracticeSolution"))


main()
