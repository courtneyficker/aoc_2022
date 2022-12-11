# Advent of Code 2022 - Day 4 Part 2
# https://adventofcode.com/2022/day/4
# Courtney Ficker

def find_overlap(e1, e2):
    lb1, rb1 = e1.strip().split('-',1)
    lb2, rb2 = e2.strip().split('-',1)

    lb1, rb1, lb2, rb2 = int(lb1), int(rb1), int(lb2), int(rb2)

    # Any matching bound means there is overlap
    # For no overlap, the right bound of one must be less than the left bound of the other
    if (rb1 < lb2 or rb2 < lb1):
        return 0
    # There must be some overlap, so count it
    return 1

with open('input.txt','r') as f:
    total = 0
    for line in f:
        e1, e2 = line.strip().split(',',1)
        total += find_overlap(e1, e2)

print(total)
