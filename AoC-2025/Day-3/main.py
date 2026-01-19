data = open("AoC-2025\\Day-3\\input.txt", "r")

results = 0

# batteryArray = [0] * 2

# print(batteryArray)

for line in data:
    line = line.strip()
    # print(line)
    formerMax, latterMax = 0, 0
    formerIndex = 0
    for i in range(len(line) - 1):
        currBattery = int(line[i])
        if currBattery > formerMax:
            formerMax = currBattery
            formerIndex = i
            if currBattery == 9:
                break

    for l in range(formerIndex + 1, len(line)):
        currBattery = int(line[l])
        if currBattery > latterMax:
            latterMax = currBattery
            if currBattery == 9:
                break

    maxBattery = int(str(formerMax) + str(latterMax))
    results += maxBattery

    # print(maxBattery)
    # print()

print(results)
