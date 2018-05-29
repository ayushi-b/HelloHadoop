#!/usr/local/bin/python3

import sys
import numpy as np


last_key = None
running_max = 0

for input_line in sys.stdin:

    input_line = input_line.strip()

    this_key, value = input_line.split("\t")

    value = float(value)

    if last_key == this_key:
        running_max = max(running_max, value)

    else:
        if last_key:
            print("{0}\t\t{1}".format(last_key, np.round(running_max, 2)))

        running_max = value
        last_key = this_key

if last_key:
    print("{0}\t\t{1}".format(last_key, np.round(running_max, 2)))
