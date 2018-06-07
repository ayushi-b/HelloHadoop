#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if len(line) != 19 or line[0] == 'id':
        continue

    time_of_post = datetime.strptime(line[8].strip()[:-3], '%Y-%m-%d %H:%M:%S.%f')
    print(line[3].strip() + "-" + str(time_of_post.hour))


