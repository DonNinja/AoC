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
            minRange, maxRange = line.split("-")
            freshRanges.append((int(minRange), int(maxRange)))

        else:
            currID = int(line)
            
            for range in freshRanges:
                if currID >= range[0] and currID <= range[1]:
                    # print("Ingredient with ID {0} is fresh.".format(line))
                    results += 1
                    break
    else:
        minRange, maxRange = line.split("-")
        
        pass


print(results)