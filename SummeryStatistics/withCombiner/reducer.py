#!/usr/local/bin/python3

import sys
import numpy as np


last_day = None
running_total = 0
sales_count = 0

for input_line in sys.stdin:

    input_line = input_line.strip()

    this_day, sales, value = input_line.split("\t")

    value = float(value)
    sales = int(sales)

    if last_day == this_day:
        running_total += value
        sales_count += sales

    else:
        if last_day:
            print("{0}\t\t{1}".format(last_day, np.round(running_total/sales_count, 2)))

        running_total = value
        sales_count = sales
        last_day = this_day

if last_day:
    print("{0}\t\t{1}".format(last_day, np.round(running_total/sales_count, 2)))