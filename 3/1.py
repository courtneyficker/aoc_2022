# Advent of Code 2022 - Day 3 Part 1
# https://adventofcode.com/2022/day/3
# Courtney Ficker

def getPrio(char):
    if (char.isupper()):
        return ord(char) - 38
    return ord(char) - 96

def findCommon(rucksack):
    length = len(rucksack)
    mid = int(length/2)

    first = rucksack[:mid]
    second = rucksack[mid:]

    for x in first:
        if (x in second):
            return x

    return None

with open('input.txt','r') as f:
    total = 0
    for line in f:
        total += getPrio(findCommon(line))

print(total)
