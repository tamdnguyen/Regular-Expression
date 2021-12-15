#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Baby name exercise: https://developers.google.com/edu/python/exercises/baby-names

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # create list named "info", which will be our final list ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    info = []

    # open and read the file
    try:
        file = open(filename, "r")
        text = file.read()
        file.close()

        # find the year
        year_match = re.search(r'input type="text" name="year" id="yob" size="4" value="(\d*?)"', text)
        if not year_match:
            print("Cannot find the year!")
            sys.exit(1)
        year = year_match.group(1)
        info.append(year)

        # find the names info
        tuples = re.findall(r'<td>(\d+?)</td><td>(\w+?)</td><td>(\w+?)</td>', text, re.IGNORECASE)
        # create a dictionary for names and their rank
        # first, create separate dictionary
        names_rank = {}
        for tuple in tuples:
            try:
                names_rank[tuple[1]] = tuple[0]
                names_rank[tuple[2]] = tuple[0]
            except IndexError:
                print("Line error:", tuple)
        # sort the dictionary by name alphabetically
        name_items = names_rank.items()
        sorted_name = sorted(name_items)

        # add the names into the final list
        for name in sorted_name:
            text = "{:s} {:d}".format(name[0], int(name[1]))
            info.append(text)
    except OSError:
        print("Cannot open {:s}.".format(filename))

    return info


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
      print('usage: [--summaryfile] file [file ...]')
      sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
      summary = True
      del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for arg in args:
        sorted_names = extract_names(arg)
        text = '\n'.join(sorted_names) + '\n'
        filename = str(arg) + ".summary"
        file = open(filename, "w")
        file.write(text + "\n")
        file.close()


if __name__ == '__main__':
    main()
