data = open("AoC-2024/Day-7/input", "r")

operators = ["*", "+", "||"]


def evaluate(values: tuple[int], operator: str) -> int:
    if operator == "*":
        return values[0] * values[1]
    elif operator == "+":
        return values[0] + values[1]
    elif operator == "||":
        return int("{}{}".format(int(values[0]), int(values[1])))

    return 0


def iterate(
    intValues: list[int], testValue: int, equation: str, resultValue: int = 0
) -> bool:
    """ Recursively iterates through the given values
        to calculate all possible permutations with
        the operators we can use
    """
    
    if resultValue > testValue:
        return False

    for i in range(1, len(intValues)):
        values = (intValues[i - 1], intValues[i])

        for op in operators:
            equation += " {} {}".format(op, intValues[i])
            evalValue = evaluate(values, op)
            newValues = [evalValue] + intValues[i + 1 :]
            if iterate(newValues, testValue, equation, evalValue):
                return True

        # By this point, we have already gone through all possible iterations and we know it won't be true
        return False

    if resultValue == testValue:
        # print("{} | {}".format(testValue, equation))
        return True
    return False


results = 0

for line in data:
    sLine = line.strip()

    testValue, calcValues = sLine.split(":")
    intValues = [int(x) for x in calcValues.strip().split(" ")]

    testValue = int(testValue)

    if iterate(intValues, testValue, str(intValues[0])):
        results += int(testValue)

print(results)

data.close()
