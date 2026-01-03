data = open("AoC-2025\\Day-2\\input.txt", "r").readline()

# print(data)

IDRanges = data.split(",")

results = 0

for IDRange in IDRanges:
    IDRangeStart, IDRangeEnd = IDRange.split("-")
    for i in range(int(IDRangeStart), int(IDRangeEnd) + 1):
        currID = str(i)
        # If an ID has an uneven length, it can't exclusively be repeated
        if len(currID) % 2 != 0:
            continue
        
        IDLength = int(len(currID) / 2)
        
        # print(currID[:IDLength], end="")
        # print(currID[IDLength:])
        formerHalf = currID[:IDLength]
        latterHalf = currID[IDLength:]
        
        if formerHalf == latterHalf:
            # print(formerHalf, latterHalf)
            results += i
        
        for l in range(int(len(currID) / 2)):
            print(currID[l], end="")
        # print()

print(results)