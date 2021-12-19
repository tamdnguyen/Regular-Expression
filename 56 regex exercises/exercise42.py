"""
Write a Python program to find urls in a string.

text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'

MODEL SOLUTION

import re
text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
print("Urls: ",urls)

"""

import re


def find_url(line):
    pattern = r'<a href="(.+?)">'
    url = re.findall(pattern, line)
    return url


def main():
    text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a>' \
           '<a href="http://github.com">Even More Examples</a>'
    url = find_url(text)
    print(url)


main()
