#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if line[0] == 'id' or len(line) != 19:
        continue

    node_type = line[5].lower()

    if node_type == 'question':
        print("{}\t{}".format(line[0], line[3]))
    elif node_type == 'answer':
        print("{}\t{}".format(line[7], line[3]))

