# Advent of Code 2022 - Day 2 Part 1
# https://adventofcode.com/2022/day/2
# Courtney Ficker

totalScore = 0

shapeScores = {
    'A' : 1,    # ROCK
    'B' : 2,    # PAPER
    'C' : 3,    # SCISSORS
    }

def decode(c):
    if (c == 'X'):  return 'A'
    if (c == 'Y'):  return 'B'
    if (c == 'Z'):  return 'C'


def matchScore(a, b):
    if (a == b):        return 3
    if (a == 'A'):
        if (b == 'B'):  return 6
        else:           return 0
    if (a == 'B'):
        if (b == 'C'):  return 6
        else:           return 0
    if (a == 'C'):
        if (b == 'A'):  return 6
        else:           return 0

with open('input.txt','r') as f:
    for line in f:
        opponent,player = line.split()
        total = shapeScores[decode(player)] + matchScore(opponent, decode(player))
        totalScore += total

print(totalScore)