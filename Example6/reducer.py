#!/usr/local/bin/python3

import sys


last_page = None
max_visits = 0
most_visited_page = None
running_total = 0

for input_line in sys.stdin:

    input_line = input_line.strip()

    data = input_line.split("\t")

    if len(data) != 2:
        continue

    this_page, value = data

    value = int(value)

    if last_page == this_page:
        running_total += value

    else:
        if last_page:
            if max_visits < running_total:
                max_visits = running_total
                most_visited_page = last_page

        running_total = value
        last_page = this_page

if last_page is not None:
    if max_visits < running_total:
        max_visits = running_total
        most_visited_page = last_page

print("{}\t\t{}".format(most_visited_page, max_visits))
