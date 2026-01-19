data = open("AoC-2025\\Day-3\\input.txt", "r")

results = 0

# batteryArray = [0] * 2

# print(batteryArray)

for line in data:
    batteryArray = [0] * 12
    line = line.strip()
    # print(line)
    formerMax, latterMax = 0, 0
    formerIndex = 0
    for b in range(len(batteryArray)):
        currMaxIndex = len(line) - (len(batteryArray) - 1 - b)
        for i in range(formerIndex, currMaxIndex):
            currBattery = int(line[i])
            if currBattery > batteryArray[b]:
                batteryArray[b] = currBattery
                formerIndex = i + 1
                if currBattery == 9:
                    break

    maxBattery = ""

    for battery in batteryArray:
        maxBattery += str(battery)

    results += int(maxBattery)

    # print(maxBattery)

print(results)
