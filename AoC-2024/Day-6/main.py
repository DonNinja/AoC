from enum import Enum

data = open("AoC-2024/Day-6/testinput.txt", "r")

guardMap = []


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for line in data:
    grid = []
    for pos in line.strip():
        grid.append(pos)
    guardMap.append(grid)
    
    pass

for w in guardMap:
    print(w)

data.close()
