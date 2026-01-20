data = open("AoC-2025\\Day-4\\input.txt", "r")

results = 0

dataArray = data.readlines()

for l in range(len(dataArray)):
    line = dataArray[l].strip()
    # print(line)
    for i in range(len(line)):
        if line[i] == "@":
            tooMany = False
            paperCount = 0
            for y in range(-1, 2):
                for x in range(-1, 2):
                    # Don't count current position
                    if y == 0 and x == 0:
                        continue

                    # Check if we won't go outside of the list
                    inXRange = i + x >= 0 and i + x < len(line)
                    inYRange = l + y >= 0 and l + y < len(dataArray)

                    if inYRange and inXRange:
                        if dataArray[l + y][i + x] == "@":
                            paperCount += 1
                            if paperCount > 3:
                                tooMany = True
                                break

                if tooMany:
                    break

            if not tooMany:
                results += 1
                    # print(dataArray[l + y][i + x], end="")
                # print()
            # print(line[i], end="")
        # print()

    # print()

print(results)
