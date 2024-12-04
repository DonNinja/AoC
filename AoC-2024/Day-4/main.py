"""
    First part should be simple of a list of lists of each line and then moving through them
"""

data = open("AoC-2024/Day-4/input", "r")

lines = [x.strip() for x in data]

word = "XMAS"

results = 0


def p1(direction: tuple, pos: tuple, depth: int) -> bool:
    if depth >= len(word):
        return True
    if direction == (1, 1):
        pass
    if (pos[0] >= 0 and pos[1] >= 0) and (pos[0] < len(lines) and pos[1] < len(lines[pos[0]])):
        if word[depth] == lines[pos[0]][pos[1]]:
            newPos = (pos[0] + direction[0], pos[1] + direction[1])
            return p1(direction, newPos, depth + 1)
    return False


for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if i == 0 and j == 2:
            pass
        if char == word[0]:
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if p1((x, y), (i, j), 0):
                        results += 1

print(results)
