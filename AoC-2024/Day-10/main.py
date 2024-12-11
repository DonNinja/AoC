data = open("AoC-2024/Day-10/testinput", "r")


def explore(topoMap, position: tuple):
    score = 0

    forks = []
    
    
    
    

    return score


topoMap = []

for line in data:
    mapLine = []
    for char in line.strip():
        mapLine.append(char)
        pass
    topoMap.append(mapLine)

result = 0

for row in range(len(topoMap)):
    for col in range(len(topoMap[row])):
        if topoMap[row][col] == "0":
            addition = explore(topoMap, (row, col), -1)
            if addition != 0:
                print(f"Exploring from {(row, col)} yielded a count of {addition}")
            # result +=
    pass

print(result)

data.close()
