file = open("AoC-2025\\Day-6\\input.txt", "r")

results = 0

data = file.readlines()

file.close()

calcArray = []

for line in data:
    entries = line.strip().split()
    if len(calcArray) == 0:
        for _ in range(len(entries)):
            calcArray.append([])
    for i in range(len(entries)):
        calcArray[i].append(entries[i])


for calc in calcArray:
    total = 0
    operator = calc[-1]
    for c in range(len(calc) - 1):
        if total == 0:
            total = int(calc[c])
        else:
            if operator == "+":
                total += int(calc[c])
            elif operator == "*":
                total *= int(calc[c])
    results += total

print(results)
