# Advent of Code 2022 - Day 6 Part 1
# https://adventofcode.com/2022/day/6
# Courtney Ficker

# 4 distinct characters => return index of 4th character

curr = []

def evaluate(c):
    def isDistinct():
        if (len(curr) != 4):
            return False
        for x in curr:
            if curr.count(x) > 1:
                return False
        return True

    curr.append(c)
    if (len(curr) == 5):
        del curr[0]
    return isDistinct()

with open('input.txt','r') as f:
    line = f.readline().strip()

    for i in range(len(line)):
        res = evaluate(line[i])
        if res:
            print(f'index {i+1}: {curr}')
            quit()
