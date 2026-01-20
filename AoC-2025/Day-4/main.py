data = open("AoC-2025\\Day-4\\testinput.txt", "r")

results = 0

dataArray = data.readlines()
paperToRemove = 1

while paperToRemove > 0:
    paperToRemove = 0

    for l in range(len(dataArray)):
        line = dataArray[l].strip()
        # print(line)
        removalLocations = []
        for i in range(len(line)):
            if line[i] == "@":
                tooMany = False
                paperCount = 0
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        # Don't count current position
                        if y == 0 and x == 0:
                            continue

                        xLoc = i + x
                        yLoc = l + y
                        # Check if we won't go outside of the list
                        inXRange = xLoc >= 0 and xLoc < len(line)
                        inYRange = yLoc >= 0 and yLoc < len(dataArray)

                        if inYRange and inXRange:
                            if dataArray[yLoc][xLoc] == "@":
                                paperCount += 1
                                if paperCount > 3:
                                    tooMany = True
                                    break

                    if tooMany:
                        break

                if not tooMany:
                    # paperToRemove += 1
                    removalLocations.append((yLoc, xLoc))
                    results += 1
                        # print(dataArray[l + y][i + x], end="")
                    # print()
                # print(line[i], end="")
            # print()

        # print()


print(results)
