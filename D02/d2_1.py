
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

rules = {'A': {'X': 3, 'Y': 6, 'Z': 0},
         'B': {'X': 0, 'Y': 3, 'Z': 6},
         'C': {'X': 6, 'Y': 0, 'Z': 3}}

moves = {'X': 1, 'Y': 2, 'Z': 3}


def score(currentGame):
    result = rules[currentGame[0]][currentGame[1]] + moves[currentGame[1]]
    print(currentGame, result)

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
