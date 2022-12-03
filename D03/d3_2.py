import numpy as np

def getPriority(c):
    basePriority = 26
    if c.islower():
        c = c.upper()
        basePriority = 0
    return ord(c)-64+basePriority

with open('example.txt', 'r') as f:
    puzzleInput = np.genfromtxt(f, dtype=str, delimiter='\n')

sum = 0
for i in range(1, len(puzzleInput), 3):
    rucksacks = [set(rucksack) for rucksack in puzzleInput[i-1:i*3]]

    x = [c for c in rucksacks[0] if c in rucksacks[1] and c in rucksacks[2]]

    print(rucksacks, x)
    prio = getPriority(x[0])
    sum += prio
    print (rucksacks, x, prio)

print(sum)
