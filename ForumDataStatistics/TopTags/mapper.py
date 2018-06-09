#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if line[0] == 'id' or len(line) != 19:
        continue

    node_type = line[5].lower()

    if node_type == 'question':
        tags = line[2].strip().split()
        for tag in tags:
            print(tag)

