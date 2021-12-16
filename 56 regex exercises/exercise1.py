# Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).

import re


def check_regex(line):
    yes_nonchar = re.search(r"([^a-zA-Z0-9])", line)
    if yes_nonchar:
        return False
    else:
        return True


def main():
    line_true = "ABCDEFabcdef123450"
    line_false = "*&%@#!}{"

    print("Line {:s} is: {:s}.".format(line_true, str(check_regex(line_true))))
    print("Line {:s} is: {:s}.".format(line_false, str(check_regex(line_false))))

main()
