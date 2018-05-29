#!/usr/local/bin/python3

import sys


last_ip = None
running_total = 0

for input_line in sys.stdin:

    input_line = input_line.strip()

    this_ip, value = input_line.split("\t")

    value = int(value)

    if last_ip == this_ip:
        running_total += value

    else:
        if last_ip:
            print("{0}\t\t{1}".format(last_ip, running_total))

        running_total = value
        last_ip = this_ip

if last_ip is not None:
    print("{0}\t\t{1}".format(last_ip, running_total))
