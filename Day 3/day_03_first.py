#!/usr/bin/python
import re

def parse_claim(claim):
    claim_ptrn = re.compile(r'\#\d+ \@ (\d+),(\d+): (\d+)x(\d+)')
    right, top, width, height = map(int, claim_ptrn.match(claim).groups())
    return right, top, width, height


def process_claim(claim, fabric):
    right, top, width, height = parse_claim(claim)
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    for i in range(top, top+height):
        for j in range(right, right+width):
            fabric[i][j] += 1


cloth = [[0 for x in range(1000)] for x in range(1000)]

with open("input.txt") as f:
    claims = f.readlines()

for claim in claims:
    process_claim(claim, cloth)

overlap = [[0 for x in range(1000)] for x in range(1000)]

for idx, row in enumerate(cloth):
    for idy, e in enumerate(row):
        if e > 1:
            overlap[idx][idy] = 1
        else:
            overlap[idx][idy] = 0

print([sum(row) for row in overlap])
