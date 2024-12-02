data = open("AoC-2024\Day-1\input.txt", "r")

sortedList = [[], []]

# Sorting the list makes the tasks easier
for line in data:
    # Split lines into 2 values
    values = line.strip().split("   ")
    values = [int(values[0]), int(values[1])]

    # Iterate through both lists
    for i in range(2):
        listIndex = 0

        # Check when the sorted list out paces the current value
        for j in range(len(sortedList[i])):
            if int(sortedList[i][j]) > int(values[i]):
                break
            listIndex += 1

        # Insert value to list at valued index
        sortedList[i].insert(listIndex, values[i])


def part1(valueList):
    """
    Simple popping from the front of both sorted lists and calculating their difference
    """

    result = 0

    while len(valueList[0]) > 0:
        val1 = valueList[0].pop()
        val2 = valueList[1].pop()

        result += abs(val1 - val2)

    print(result)


def part2(valueList):
    """
    Instead of going through the list every time there is a new number,
    add them into a dictionary which have an O(1) lookup time.
    """

    numCount = {}
    results = 0

    for value in valueList[0]:
        counter = 0

        if value in numCount:
            results += value * numCount[value]
            continue
        else:
            for number in valueList[1]:
                if number == value:
                    counter += 1
                elif value < number:
                    results += value * counter
                    numCount[value] = counter
                    break

    print(results)


# print(sortedList)
part1(sortedList)

data.close()
