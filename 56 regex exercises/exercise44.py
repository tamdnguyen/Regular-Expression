"""
Write a Python program to do a case-insensitive string replacement.

EXPLANATION OF TASK

Input : test_str = “gfg is BeSt”, repl = “good”, subs = “best”

Output : gfg is good

Explanation : BeSt is replaced by “good” ignoring cases.

Input : test_str = “gfg is BeSt”, repl = “better”, subs = “best”

Output : gfg is better

Explanation : BeSt is replaced by “better” ignoring cases.
"""

import re


def main():
    test_str = "gfg is BeSt"
    replace = "good"
    subs = "best"

    compiled = re.compile(re.escape(subs), re.IGNORECASE)
    str_after = re.sub(compiled, replace, test_str)
    print(str_after)


main()

