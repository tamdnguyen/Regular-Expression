# Write a Python program to replace whitespaces with an underscore and vice versa.

import re


def replace(line):
    whitespace_underscore = r"\s"
    underscore_whitespace = r"_"

    if re.search(whitespace_underscore, line):
        change_whitespace = re.sub(whitespace_underscore, "_", line)
        print("Replace whitespace by underscore successfully")
        return change_whitespace
    elif re.search(underscore_whitespace, line):
        change_underscore = re.sub(underscore_whitespace, " ", line)
        print("Replace underscore by whitespace successfully")
        return change_underscore


def main():
    text = 'Python Exercises'
    print(replace(text))
    text2 = 'Python_Exercises'
    print(replace(text2))


main()