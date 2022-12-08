# Advent of Code 2022 - Day 2 Part 1
# https://adventofcode.com/2022/day/2
# Courtney Ficker

totalScore = 0

shapeScores = {
    'A' : 1,    # ROCK
    'B' : 2,    # PAPER
    'C' : 3,    # SCISSORS
    }

matchScores = {'WIN'  : 6, 'LOSE' : 0, 'DRAW' : 3}
winChoice =     {'A' : 'B', 'B' : 'C', 'C' : 'A'}
loseChoice =    {'A' : 'C', 'B' : 'A', 'C' : 'B'}

def drawScore(opp):
    return shapeScores[opp] + matchScores['DRAW']

def winScore(opp):
    return shapeScores[winChoice[opp]] + matchScores['WIN']

def loseScore(opp):
    return shapeScores[loseChoice[opp]] + matchScores['LOSE']

with open('input.txt','r') as f:
    for line in f:
        opponent,player = line.split()
        if (player == 'X'): totalScore += loseScore(opponent)
        if (player == 'Y'): totalScore += drawScore(opponent)
        if (player == 'Z'): totalScore += winScore(opponent)

print(totalScore)