data = open("AoC-2024/Day-7/testinput.txt", "r")

operators = ["*", "+"]

def evaluate(values, operator):
    if operator == "*":
        return values[0] * values[1]
    elif operator == "+":
        return values[0] + values[1]
    
    return 0
    pass

for line in data:
    sLine = line.strip()
    
    testValue, calcValues = sLine.split(":")
    intValues = [int(x) for x in calcValues.strip().split(" ")]
    
    pass

data.close()