"""
Write a Python program that takes any number of iterable objects or objects with a length property
and returns the longest one.

Input:
print(longest_item('Red', 'Green', 'Black', 'Orange'))
print(longest_item([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))
print(longest_item([1, 2, 3], 'Java'))
print(longest_item({10, 100}, 'Python'))

Sample Output:
Orange
[1, 2, 3, 4, 5]
Java
Python

MODEL SOLUTION

def longest_item(*args):
  return max(args, key = len)

print(longest_item('Red', 'Green', 'Black', 'Orange'))
print(longest_item([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))
print(longest_item([1, 2, 3], 'Java'))
print(longest_item({10, 100}, 'Python'))

"""


def longest_item(*args):
    max_len = len(args[0])
    for obj in args:
        if max_len < len(obj):
            max_len = len(obj)
            index = args.index(obj)

    return args[index]


print(longest_item('Red', 'Green', 'Black', 'Orange'))
print(longest_item([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))
print(longest_item([1, 2, 3], 'Java'))
print(longest_item({10, 100}, 'Python'))
