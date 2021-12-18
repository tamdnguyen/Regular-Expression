"""
Write a Python program to separate and print the numbers of a given string.
# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"

MODEL SOLUTION

import re
# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
# Print results.
for element in result:
    print(element)

"""
import re


def separate(line):
    pattern = r"[0-9]+"
    nums = re.findall(pattern, line)
    return nums


def main():
    text = "Ten 10, Twenty 20, Thirty 30"
    nums = separate(text)
    for num in nums:
        print(num)


main()
