#!/usr/local/bin/python3

import sys


last_word = None
word_index = set([])
current_count = 0

for input_line in sys.stdin:

    data = input_line.strip().split("\t")

    if len(data) != 2:
        continue

    this_word, node_id = data
    node_id = int(node_id)

    if last_word == this_word:
        word_index.add(node_id)
        current_count += 1

    else:
        if last_word:
            if current_count < 10:
                print("{}\t{}\t{}".format(last_word, sorted(word_index), current_count))
            else :
                print("{}\t{}".format(last_word, current_count))

        word_index = set([node_id])
        last_word = this_word
        current_count = 1

if last_word:
    if current_count < 10:
        print("{}\t{}\t{}".format(last_word, sorted(word_index), current_count))
    else:
        print("{}\t{}".format(last_word, current_count))
