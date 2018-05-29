#!/usr/local/bin/python3

import sys
import numpy as np

total_sales = 0
total_value = 0

for input_line in sys.stdin:

    input_line = input_line.strip()

    count, value = input_line.split("\t")

    total_value += float(value)
    total_sales += int(count)


print("{0}\t\t{1}".format(total_sales, np.round(total_value, 2)))
