"""Write a Python program to extract year, month and date from an url.
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-
on-one-stupid-little-ball-josh-norman-tells-author/"


"""

import re


def extract(line):
    total_date = re.search(r"/([0-9]{4})/([0-9]{1,2})/([0-9]{1,2})/", line)
    if total_date:
        print("Found the date in the url")
        print("Year:", total_date.group(1))
        print("Month:", total_date.group(2))
        print("Date:", total_date.group(3))
    else:
        print("No date in the url")


def main():
    url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-" \
          "on-one-stupid-little-ball-josh-norman-tells-author/"
    extract(url)


main()
