#!/usr/bin/python

import sys
import csv
import numpy as np

reader = csv.reader(sys.stdin, delimiter='\t')
current_question_id = None
question_length = 0
current_qalength_sum = 0
ans_count = 0

for line in reader:

    node, length = line
    node_id, node_type = node.strip().split('-')
    length = float(length)

    if node_type == 'A':
        if current_question_id:
            if ans_count == 0:
                ans_count = 1
            print("{}\t{}\t{}".format(
                current_question_id,
                question_length,
                np.around(current_qalength_sum/ans_count, 2)
            ))
        current_question_id = node_id
        current_qalength_sum = 0
        question_length = int(length)
        ans_count = 0
    elif node_type == 'B':
        if current_question_id == node_id:
            current_qalength_sum += length
            ans_count += 1


if current_question_id:
    if ans_count == 0:
        ans_count = 1
    print("{}\t{}\t{}".format(
        current_question_id,
        question_length,
        np.around(current_qalength_sum/ans_count, 2)
    ))
