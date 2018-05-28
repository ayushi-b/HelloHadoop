#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split("\t")

    if len(keys) < 6:
        continue

    date, time, store, product, cost, mode = keys

    print("{}\t{}".format(store, cost))
