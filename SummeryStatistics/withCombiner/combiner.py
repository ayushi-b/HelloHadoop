#!/usr/local/bin/python3

import sys


last_day = None
running_total = 0
sales_count = 0

for input_line in sys.stdin:

    input_line = input_line.strip()

    this_day, value = input_line.split("\t")

    value = float(value)

    if last_day == this_day:
        running_total += value
        sales_count += 1

    else:
        if last_day:
            print("{0}\t{1}\t{2}".format(last_day, sales_count, running_total))

        running_total = value
        sales_count = 1
        last_day = this_day

if last_day:
    print("{0}\t{1}\t{2}".format(last_day, sales_count, running_total))
