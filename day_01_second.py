#!/usr/bin/python

from itertools import cycle
with open("./input.txt") as f:
    phases = cycle(f.readlines())

seen = set()

frequency = 0

while frequency not in seen:
    seen.add(frequency)
    frequency += int(next(phases))

print(frequency)
