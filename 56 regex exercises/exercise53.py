"""
Write a Python program to remove lowercase substrings from a given string.

Sample Output:

Original string:
KDeoALOklOOHserfLoAJSIskdsf
After removing lowercase letters, above string becomes:
KDALOOOHLAJSI

MODEL SOLUTION (very good, using lambda and re.sub(). Better than my code actually)

import re
str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
print("Original string:")
print(str1)
print("After removing lowercase letters, above string becomes:")
remove_lower = lambda text: re.sub('[a-z]', '', text)
result =  remove_lower(str1)
print(result)

"""

import re


def remove(line):
    lower = re.compile(r"([^a-z+]|^)([a-z]+)")
    return lower.sub(r"\1", line)


def main():
    text = "KDeoALOklOOHserfLoAJSIskdsf"
    text1 = "jkhdfjkAJHLAFHlhjflakshflakshflhLJASHFLKAHDF;fhksdfhsdkjfF;SKHFDdfkhskjshJjJhLHloHNOo"
    print(remove(text))
    print(remove(text1))


main()
