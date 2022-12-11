# Advent of Code 2022 - Day 4 Part 1
# https://adventofcode.com/2022/day/4
# Courtney Ficker

def find_enclosure(e1, e2):
    lb1, rb1 = e1.strip().split('-',1)
    lb2, rb2 = e2.strip().split('-',1)

    lb1, rb1, lb2, rb2 = int(lb1), int(rb1), int(lb2), int(rb2)

    # Any matching bound means something is fully contained by definition.
    # Find non-matches and return 1 by default
    if (lb1 < lb2 and rb1 < rb2):
        return 0
    if (lb2 < lb1 and rb2 < rb1):
        return 0
    return 1

with open('input.txt','r') as f:
    total = 0
    for line in f:
        e1, e2 = line.strip().split(',',1)
        total += find_enclosure(e1, e2)

print(total)
