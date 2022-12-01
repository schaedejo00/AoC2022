import numpy as np

with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

sum = 0
maximum = 0
for value in puzzleInput:
    if value == '':
        maximum = max(sum, maximum)
        sum = 0
    else:
        sum += int(value)

print(maximum)

