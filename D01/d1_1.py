import numpy as np
from numpy import sort

with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

sum = 0
sums = []
for value in puzzleInput:
    if value == '':
        sums.append(sum)
        sum = 0
    else:
        sum += int(value)

print(np.sum(sort(sums)[-3:]))

