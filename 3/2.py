# Advent of Code 2022 - Day 3 Part 2
# https://adventofcode.com/2022/day/3
# Courtney Ficker

def getPrio(char):
    if (char.isupper()):
        return ord(char) - 38
    return ord(char) - 96

def findCommon(rucksack):
    first = rucksack[0]
    second = rucksack[1]
    third = rucksack[2]

    for x in first:
        if (x in second):
            if (x in third):
                return x

    return None

with open('input.txt','r') as f:
    rucksacks = []
    total = 0
    for line in f:
        rucksacks.append(line)
        if (len(rucksacks) == 3):
            total += getPrio(findCommon(rucksacks))
            rucksacks.clear()

print(total)
