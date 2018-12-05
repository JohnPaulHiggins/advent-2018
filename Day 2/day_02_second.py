#!/usr/bin/python
from itertools import combinations

def compare_ids(box1, box2):
    id1 = list(map(ord, list(box1)))
    id2 = list(map(ord, list(box2)))

    return [(id1[i] - id2[i]) for i in range(len(id1))]


with open("./input.txt") as f:
    boxes = f.readlines()

comparisons = list(combinations(range(len(boxes)), 2))

diffs = [compare_ids(boxes[tup[0]],
                     boxes[tup[1]]) for tup in comparisons]

for comp_num, comp_id in enumerate(diffs):
    if len(set(comp_id)) == 2 and comp_id.count(0) == (len(comp_id) - 1):
        correct_id1, correct_id2 = (boxes[comparisons[comp_num][0]],
                                    boxes[comparisons[comp_num][1]])
        correct_offset = comp_id

diff_letter_idx = [i for i, e in enumerate(correct_offset) if e != 0][0]
# Thank you Ignacio Vazquez-Abrams from Stack Overflow

print(correct_id1[:diff_letter_idx] + correct_id1[diff_letter_idx+1:])
