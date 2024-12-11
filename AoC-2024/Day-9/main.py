data = open("AoC-2024/Day-9/input", "r")

filesystemLine = []

line = data.readline().strip()

added = 0

for i in range(len(line)):
    if i % 2 != 0:
        filesystemLine += "." * int(line[i])
        pass
    else:
        for i in range(int(line[i])):
            filesystemLine.append(str(added))
            pass
        added += 1
        pass

    pass

added -= 1

# print(filesystemLine)

fullBreak = False

dotIndex = 0

for i in range(len(filesystemLine) - 1, -1, -1):
    if fullBreak:
        break

    for j in range(dotIndex, len(filesystemLine)):
        if i <= j:
            fullBreak = True
            break
        if filesystemLine[j] == ".":
            x = filesystemLine[i]
            y = filesystemLine[j]
            filesystemLine[i] = y
            filesystemLine[j] = x
            dotIndex = j
            # filesystemLine = filesystemLine[:j] + x + filesystemLine[j+1:i]
            break
        pass

results = 0

for i in range(len(filesystemLine)):
    if filesystemLine[i] == ".":
        break
    results += i * int(filesystemLine[i])
    # print(filesystemLine[i], end='')
    pass

# print()

print(results)

data.close()
