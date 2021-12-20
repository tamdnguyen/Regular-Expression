"""
Write a Python program that reads a given expression and evaluates it.
Terms and conditions:
The expression consists of numerical values, operators and parentheses, and the ends with '='.
The operators includes +, -, *, / where, represents, addition, subtraction, multiplication and division.
When two operators have the same precedence, they are applied to left to right.
You may assume that there is no division by zero.
All calculation is performed as integers, and after the decimal point should be truncated
Length of the expression will not exceed 100.
-1 ? 10 9 = intermediate results of computation = 10 9

"""
# Hi
import re


def main():
    cases = int(input("Input number of data sets:\n"))
    for i in range(cases):
        line = input("Input an expression:\n")
        expression = re.search(r"[0-9+\*\/\(\)-]+=", line)
        print(eval(expression.group()[:-1]))


main()
