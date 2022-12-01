# Advent of Code 2022 - Day 1 Part 1
# https://adventofcode.com/2022/day/1
# Courtney Ficker

# Cliff's Notes:
#   Read in lists of numbers separated by blank lines, sum each chunk.
#   Return the largest total

maxTotal = 0

with open('../input.txt','r') as f:
    total = 0
    for line in f:
        n = line.strip()
        if n.isnumeric():
            total += int(n)
        else:
            if total > maxTotal:
                maxTotal = total
            total = 0

print(maxTotal)
