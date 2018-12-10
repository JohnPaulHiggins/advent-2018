#!/usr/bin/python
from itertools import combinations
import re

def parse_claim(claim):
    claim_ptrn = re.compile(r'\#\d+ \@ (\d+),(\d+): (\d+)x(\d+)')
    right, top, width, height = map(int, claim_ptrn.match(claim).groups())
    return right, top, width, height


def overlap(claim1, claim2):
    right1, top1, width1, height1 = parse_claim(claim1)
    right2, top2, width2, height2 = parse_claim(claim2)

    xrange_1 = set(range(right1, right1+width1))
    yrange_1 = set(range(top1, top1+height1))
    xrange_2 = set(range(right2, right2+width2))
    yrange_2 = set(range(top2, top2+height2))

    if (xrange_1 & xrange_2) and (yrange_1 & yrange_2):
        return True
    else:
        return False


with open("input.txt") as f:
    claims = f.readlines()

ids = set(range(len(claims)))

for idn in ids:
    if not any([overlap(claims[idn], claims[idx]) for idx in (ids - {idn})]):
        print(idn+1)

