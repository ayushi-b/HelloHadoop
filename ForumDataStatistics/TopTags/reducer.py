#!/usr/bin/python

import sys

top_n = list(zip([chr(i+65) for i in range(10)], [0]*10))
last_tag = None
tag_count = 0

for line in sys.stdin:

    current_tag = line.strip()
    if last_tag == current_tag:
        tag_count += 1
    else:
        if last_tag:
            if tag_count > top_n[0][1]:
                top_n[0] = (last_tag, tag_count)
                top_n = sorted(top_n, key=lambda x: x[1])

        last_tag = current_tag
        tag_count = 1


if last_tag:
    if tag_count > top_n[0][1]:
        top_n[0] = (last_tag, tag_count)
        top_n = sorted(top_n, key=lambda x: x[1])

for data in top_n[::-1]:
    tag, tag_count = data
    print("{}\t{}".format(tag, tag_count))

