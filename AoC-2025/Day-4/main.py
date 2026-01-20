data = open("AoC-2025\\Day-4\\testinput.txt", "r")

results = 0
lineNum = 0

for line in data:
    line = line.strip()
    # print(line)
    for i in range(len(line)):
        print(line[i], end="")
    
    print()
    
    lineNum += 1

# print(results)
