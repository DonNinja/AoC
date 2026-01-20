data = open("AoC-2025\\Day-4\\input.txt", "r")

results = 0

dataArray = data.readlines()

while True:
    # Create a list of locations to remove toilet paper from
    removalLocations = []

    for l in range(len(dataArray)):
        line = dataArray[l].strip()
        # print(line)
        for i in range(len(line)):
            if line[i] == "@":
                tooMany = False
                paperCount = 0
                
                # Look in a circle around it
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        # Don't count current position
                        if y == 0 and x == 0:
                            continue

                        # Calculate the search locations
                        xLoc = i + x
                        yLoc = l + y

                        # Check if we won't go outside of the list
                        inXRange = xLoc >= 0 and xLoc < len(line)
                        inYRange = yLoc >= 0 and yLoc < len(dataArray)

                        if inYRange and inXRange:
                            if dataArray[yLoc][xLoc] == "@":
                                paperCount += 1
                                if paperCount > 3:
                                    # No need to keep searching if we have already decided to not remove it
                                    tooMany = True
                                    break
                                    
                    if tooMany:
                        break

                if not tooMany:
                    removalLocations.append((l, i))
                    results += 1
                    # print(dataArray[l + y][i + x], end="")
                    # print()
                # print(line[i], end="")
            # print()

        # print()
    if len(removalLocations) > 0:
        for y, x in removalLocations:
            tempString = ""
            for i in range(len(dataArray[y])):
                if (i == x):
                    tempString += "."
                else:
                    tempString += dataArray[y][i]
            dataArray[y] = tempString
    else:
        break


print(results)
