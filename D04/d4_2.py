from typing import Set

import numpy as np

count = 0
with open('input_1.txt', 'r') as f:
    line = f.readline().replace("\n","")
    while line:
        line = [token.split("-") for token in line.split(",")]
        left: Set[int] = set(np.arange(int(line[0][0]), int(line[0][1])+1, 1))
        right: Set[int] = set(np.arange(int(line[1][0]), int(line[1][1]) + 1, 1))

        intersection: Set[int] = left & right
        if len(intersection) > 0:
            count+=1

        print(line, left, right, intersection)
        line = f.readline().replace("\n","")
print (count)

