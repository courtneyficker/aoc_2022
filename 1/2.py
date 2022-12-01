# Advent of Code 2022 - Day 1 Part 2
# https://adventofcode.com/2022/day/1
# Courtney Ficker

# Cliff's Notes:
#   Read in lists of numbers separated by blank lines, sum each chunk.
#   Return sum of the THREE largest totals

top3 = [0,0,0,0]

def rank_top3(num):
    top3[3] = num
    top3.sort(reverse=True)

def get_top3():
    return top3[0] + top3[1] + top3[2]

with open('../input.txt','r') as f:
    total = 0
    for line in f:
        n = line.strip()
        if n.isnumeric():
            total += int(n)
        else:
            rank_top3(total)
            total = 0

print(get_top3())
