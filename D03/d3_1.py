import numpy as np

def getPriority(c):
    basePriority = 26
    if c.islower():
        c = c.upper()
        basePriority = 0
    return ord(c)-64+basePriority

with open('input_1.txt', 'r') as f:
    puzzleInput = np.genfromtxt(f, dtype=str, delimiter='\n')

sum = 0
for rucksack in puzzleInput:
    firstCompartment, secondCompartment = set(rucksack[:int(len(rucksack) / 2)]), set(rucksack[int(len(rucksack) / 2):])

    x = [c for c in firstCompartment if c in secondCompartment]

    prio = getPriority(x[0])
    sum += prio
    print (rucksack, x, prio)

print(sum)
