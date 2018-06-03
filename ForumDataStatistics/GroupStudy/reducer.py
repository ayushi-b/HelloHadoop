#!/usr/bin/python

import sys
import csv

last_post_id = None
user_ids = []

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    post_id, user_id = line
    user_id = int(user_id)

    if post_id == last_post_id:
        user_ids.append(user_id)
    else:
        if last_post_id:
            print("{}\t{}".format(last_post_id, user_ids))
        user_ids = [user_id]
        last_post_id = post_id


if last_post_id:
    print("{}\t{}".format(last_post_id, user_ids))
