"""
Write a Python program to remove the parenthesis area in a string. Go to the editor
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output:
example
w3resource
github
stackoverflow

"""

import re


def remove(line):
    parenthesis = re.compile(r"\(.*\)")
    return parenthesis.sub("", line)


def main():
    datas = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
    for data in datas:
        print(remove(data))


main()
