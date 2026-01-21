file = open("AoC-2025\\Day-5\\input.txt", "r")

results = 0

data = file.readlines()

file.close()

rangeFinding = True
freshCheck = False

freshRanges = []

for line in data:
    line = line.strip()
    # print(line)

    if line == "":
        if freshCheck:
            print("Range finding finished")
            rangeFinding = False
            continue
        else:
            break

    if freshCheck:
        if rangeFinding:
            minID, maxID = line.split("-")
            freshRanges.append((int(minID), int(maxID)))

        else:
            currID = int(line)

            for fRange in freshRanges:
                if currID >= fRange[0] and currID <= fRange[1]:
                    results += 1
                    break
    else:
        minID, maxID = line.split("-")
        minID = int(minID)
        maxID = int(maxID)

        minRangeIndex, maxRangeIndex = -1, -1

        for i in range(len(freshRanges)):
            fRange = freshRanges[i]

            if fRange[1] >= minID and fRange[0] <= minID:
                minRangeIndex = i

            if fRange[0] <= maxID and fRange[1] >= maxID:
                maxRangeIndex = i

        if minRangeIndex != maxRangeIndex:
            minRange = freshRanges[minRangeIndex]
            maxRange = freshRanges[maxRangeIndex]

            if maxRangeIndex == -1:
                freshRanges[minRangeIndex] = (minRange[0], maxID)
            elif minRangeIndex == -1:
                freshRanges[maxRangeIndex] = (minID, maxRange[1])
            else:
                freshRanges[minRangeIndex] = (minRange[0], maxRange[1])
                freshRanges.pop(maxRangeIndex)
        elif minRangeIndex == -1 and maxRangeIndex == -1:
            freshRanges.append((minID, maxID))
            # pass
        pass
    
freshRanges.sort()

if not freshCheck:
    for r in freshRanges:
        results += r[1] - r[0]
        # results += 1

print(results)
