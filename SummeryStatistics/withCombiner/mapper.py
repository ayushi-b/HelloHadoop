#!/usr/local/bin/python3

import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    keys = line.split("\t")

    if len(keys) < 6:
        continue

    date, time, store, product, cost, mode = keys

    weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

    print("{}\t{}".format(weekday, cost))

