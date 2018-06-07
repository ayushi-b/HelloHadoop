#!/usr/bin/python

import sys

last_user_id = None
last_user_hr = None

current_hr_count = 0

user_max_count = 0
user_max_hr = None

for line in sys.stdin:

    this_user_id, this_user_hr = line.strip().split('-')

    if this_user_id == last_user_id:
        if last_user_hr == this_user_hr:
            current_hr_count += 1
        else:
            if user_max_count < current_hr_count:
                user_max_count = current_hr_count
                user_max_hr = [last_user_hr]
            elif user_max_count == current_hr_count:
                user_max_hr.append(last_user_hr)
            current_hr_count = 1
    else:
        if last_user_id:
            if user_max_count < current_hr_count:
                user_max_count = current_hr_count
                user_max_hr = [last_user_hr]
            elif user_max_count == current_hr_count:
                user_max_hr.append(last_user_hr)
            for max_hr in user_max_hr:
                print("{}\t{}".format(last_user_id, max_hr))

        current_hr_count = 1
        user_max_hr = [this_user_hr]
        user_max_count = 0

    last_user_id = this_user_id
    last_user_hr = this_user_hr


if last_user_id:
    if user_max_count < current_hr_count:
        user_max_count = current_hr_count
        user_max_hr = [last_user_hr]
    elif user_max_count == current_hr_count:
        user_max_hr.append(last_user_hr)
    for max_hr in user_max_hr:
        print("{}\t{}".format(last_user_id, max_hr))




