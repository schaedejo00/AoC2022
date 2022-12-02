import numpy as np
from numpy import sort
#A for Rock, B for Paper, and C for Scissors
#Rock 1, Paper 2, Scissors 3
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

moves = {'A':{'X':3, 'Y':1, 'Z':2},
         'B':{'X':1, 'Y':2, 'Z':3},
         'C':{'X':2, 'Y':3, 'Z':1}}

res = {'X':0, 'Y':3, 'Z':6}

def score(game):
    result = moves[game[0]][game[1]] + res[game[1]]
    print(game, result)

    return result


puzzleInput = []
with open('input_1.txt', 'r') as f:
    line = f.readline().replace("\n", "")
    while line:
        puzzleInput.append(line.split(" "))
        line = f.readline().replace("\n", "")
sum = 0
for game in puzzleInput:
    sum += score(game)

print(sum)

