#!/usr/local/bin/python3

import sys
import re


parts = [
    r'(?P<ip>\S+)',                     # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
]

pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')

for line in sys.stdin:

    m = pattern.match(line)

    if m is None:
        continue

    res = m.groupdict()

    page = res['request'].split()[1]

    if page == '/assets/js/the-associates.js':
        print("{}\t{}".format(page, 1))


