#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
current_user_id = None
current_user_data = None

for line in reader:

    user_id = line[0]
    this_user_id = user_id[:-1]
    file = user_id[-1]

    if file == 'A':
        current_user_id = this_user_id
        current_user_data = line[1:]
    elif file == 'B':
        if this_user_id == current_user_id:
            data = [current_user_id, line[3], line[1], line[2]]
            data.extend(line[4:])
            data.extend(current_user_data)
            print("\t".join(data))



