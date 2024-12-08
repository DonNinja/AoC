import re


class Position:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __sub__(self, otherPos):
        return Position(self.y - otherPos.y, self.x - otherPos.x)

    def __add__(self, otherPos):
        return Position(self.y + otherPos.y, self.x + otherPos.x)

    def __neg__(self):
        return Position(self.y * -1, self.x * -1)

    def __lt__(self, otherPos):
        return self.y < otherPos.y and self.x < otherPos.x

    def __str__(self):
        return f"{self.y} | {self.x}"

    def get(self):
        return (self.y, self.x)


data = open("AoC-2024/Day-8/input", "r")

lines = data.readlines()

locations = []

locMap = []

for y in range(len(lines)):
    locLine = []
    l = lines[y].strip()

    for x in range(len(l)):
        if re.match(r"[0-9a-zA-Z]", l[x]):
            locations.append((l[x], Position(y, x)))
            pass
        locLine.append(l[x])
        pass
    locMap.append(locLine)

locations.sort()

for i in range(len(locations)):
    currentLoc = locations[i]

    for j in range(i + 1, len(locations)):
        checkLoc = locations[j]
        if checkLoc[0] != currentLoc[0]:
            break
        else:
            currPos: Position = currentLoc[1]
            checkPos: Position = checkLoc[1]
            vector: Position = currPos - checkPos

            newCurrLoc = currPos + vector
            newCheckLoc = checkPos + (-vector)

            currCheckY = newCurrLoc.y < len(locMap) and newCurrLoc.y >= 0
            currCheckX = newCurrLoc.x < len(locMap[0]) and newCurrLoc.x >= 0

            if currCheckY and currCheckX:
                locMap[newCurrLoc.y][newCurrLoc.x] = "#"

            checkCheckY = newCheckLoc.y < len(locMap) and newCheckLoc.y >= 0
            checkCheckX = newCheckLoc.x < len(locMap[0]) and newCheckLoc.x >= 0

            if checkCheckX and checkCheckY:
                locMap[newCheckLoc.y][newCheckLoc.x] = "#"

        pass
    pass

results = 0

for line in locMap:
    for char in line:
        if char == "#":
            results += 1
        print(char, end="")
    print()

print(results)

data.close()
