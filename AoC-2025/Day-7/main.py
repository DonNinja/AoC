file = open("AoC-2025\\Day-7\\testinput.txt", "r")

results = 0

data = file.readlines()

file.close()

diagramMatrix = []

tachyonLocations = []

# Fill the diagram matrix so we can start navigating through it
for line in data:
    line = line.strip()
    diagramLine = []
    for char in line:
        diagramLine.append(char)
    
    diagramMatrix.append(diagramLine)
    
