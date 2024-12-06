data = open("AoC-2024/Day-6/input.txt", "r")

guardMap = []

results = 0

movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

directions = {"^": 0, ">": 1, "v": 2, "<": 3}

movementIndex = 0
move = (0, 0)
guardLocation = [0, 0]
i = 0


for line in data:
    j = 0
    grid = []
    for pos in line.strip():
        if directions.get(pos) != None:
            movementIndex = directions[pos]
            move = movements[movementIndex]
            guardLocation = [i, j]
        grid.append(pos)
        j += 1
    guardMap.append(grid)

    i += 1
    pass

guardLocX, guardLocY = guardLocation[1], guardLocation[0]
# print(guardMap[guardLocY][guardLocX])
nextLocX = guardLocX + move[1]
nextLocY = guardLocY + move[0]

while (nextLocX >= 0 and nextLocX < len(guardMap[guardLocY])) and (
    nextLocY >= 0 and nextLocY < len(guardMap)
):
    nextLocation = guardMap[guardLocY + move[0]][guardLocX + move[1]]
    currLocation = guardMap[guardLocY][guardLocX]
    
    if currLocation != "X":
        results += 1
        guardMap[guardLocY][guardLocX] = "X"
    
    if nextLocation == "#":
        movementIndex = (movementIndex + 1) % 4
        move = movements[movementIndex]
    
    # print(nextLocation)

    guardLocation[0] += move[0]
    guardLocation[1] += move[1]
    guardLocX, guardLocY = guardLocation[1], guardLocation[0]
    nextLocX = guardLocX + move[1]
    nextLocY = guardLocY + move[0]

if currLocation != "X":
    results += 1
    guardMap[guardLocY][guardLocX] = "X"

# for m in guardMap:
    # print(m)
    
print(results)

data.close()
