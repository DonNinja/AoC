"""
    First part should be simple of a list of lists of each line and then moving through them
"""

data = open("AoC-2024/Day-4/testinput", "r")

lines = [x.strip() for x in data]

word = "XMAS"

results = 0

startPostions = []


def p1(direction: tuple, pos: tuple, depth: int) -> bool:
    if depth >= len(word):
        return True
    if word[depth] == lines[pos[0]][pos[1]]:
        newPos = (pos[0] + direction[0], pos[1] + direction[1])
        return p1(direction, newPos, depth + 1)
    return False


for i in range(len(lines)):
    for j in range(len(lines[i])):
        for x in range(-1, 1):
            for y in range(-1, 1):
                if p1((i, j), (x, y), 0):
                    results += 1

print(results)
