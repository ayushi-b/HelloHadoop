#!/usr/local/bin/python3

import sys
import csv
import re

data = csv.reader(sys.stdin, delimiter='\t')

col_names = None
for line in data:

    col_names = line
    break


tags_cleaner = re.compile('<.*?>')

for line in data:

    line_dict = dict(zip(col_names, line))
    try:
        body = re.sub(tags_cleaner, '', line_dict['body'].strip().lower())
        body = re.sub('[^a-z]+', ' ', body)
        body = body.split()
    except KeyError:
        continue

    for word in body:
        if word != "":
            print("{}\t{}".format(word, line_dict['id']))


