file = open("AoC-2025\\Day-7\\testinput.txt", "r")

results: int = 0

data = file.readlines()

file.close()

diagramMatrix: list[list] = []

tachyonLocations: list[tuple] = []

# Fill the diagram matrix so we can start navigating through it
for line in data:
    line = line.strip()
    diagramLine = []
    for char in line:
        diagramLine.append(char)

    diagramMatrix.append(diagramLine)

tachyonLocations.append((diagramMatrix[0].index("S"), 0))

while len(tachyonLocations) > 0:
    currLoc = tachyonLocations.pop(0)
    if currLoc[1] == len(diagramMatrix) - 1:
        continue
    downPos = diagramMatrix[currLoc[1] + 1][currLoc[0]]
    
    if downPos == ".":
        tachyonLocations.append((currLoc[0], currLoc[1] + 1))
    elif downPos == "^":

        if tachyonLocations:
            tachyonLocations.append((currLoc[0] - 1, currLoc[1] + 1))
        tachyonLocations.append((currLoc[0] + 1, currLoc[1] + 1))
        results += 1

print(results)