"""
Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
date1 = "2026-01-02"
date2 = "2002-11-21"

"""

import re


def convert(line):
    date = re.search(r"([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})", line)
    if date:
        print('Found valid date from "{:s}"'.format(line))
        print("Old format: {:s}".format(line))
        year = date.group(1)
        month = date.group(2)
        day = date.group(3)
        print("New format: {:s}-{:s}-{:s}".format(day, month, year))
    else:
        print("Cannot find the date")


def main():
    date1 = "2026-01-02"
    date2 = "2002-11-21"
    date3 = "No date here"
    date4 = "This is a paper from the old date 1945-9-2"

    convert(date1)
    convert(date2)
    convert(date3)
    convert(date4)


main()
