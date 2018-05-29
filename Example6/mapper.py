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

    url = 'http://www.the-associates.co.uk'
    l_url = len(url)
    page = res['request'].split()[1]

    if url in page:
        page = page[l_url:]

    print("{}\t{}".format(page, 1))


