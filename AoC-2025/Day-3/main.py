data = open("AoC-2025\\Day-3\\input.txt", "r")

results = 0

for line in data:
    # A dynamic array for battery allocation
    batteryArray = [0] * 12

    line = line.strip()

    # Save where the former battery found its max number
    formerIndex = 0

    # Iterate through all the batteries
    for batteryIndex in range(len(batteryArray)):
        # Calculate how far the current battery is allowed to look
        maxIndexOffset = len(batteryArray) - 1 - batteryIndex
        currMaxIndex = len(line) - maxIndexOffset

        for i in range(formerIndex, currMaxIndex):
            currBattery = int(line[i])
            if currBattery > batteryArray[batteryIndex]:
                batteryArray[batteryIndex] = currBattery
                formerIndex = i + 1
                # If the current battery has a power of 9, we can't add a bigger number to the current index
                if currBattery == 9:
                    break

    maxBattery = ""

    for battery in batteryArray:
        maxBattery += str(battery)

    results += int(maxBattery)

    # print(maxBattery)

print(results)
