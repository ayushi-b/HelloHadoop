#!/usr/local/bin/python3

import sys


last_file = None
running_total = 0

for input_line in sys.stdin:

    input_line = input_line.strip()

    this_file, value = input_line.split("\t")

    value = int(value)

    if last_file == this_file:
        running_total += value

    else:
        if last_file:
            print("{0}\t\t{1}".format(last_file, running_total))

        running_total = value
        last_file = this_file

if last_file is not None:
    print("{0}\t\t{1}".format(last_file, running_total))
