data = open("AoC-2025\\Day-1\\input.txt", "r")

dialMax = 100
dialMin = 0

dialDir = 50

count = 0

#
for line in data:
    line = line.strip()

    # print(dialDir)

    direction = line[0]
    rotation = int(line[1:])
    
    rotation -= (rotation // dialMax) * dialMax
    
    if direction == "L":
        rotation *= -1
    
    dialDir += rotation
    
    dialDir = dialDir % dialMax

    if dialDir == 0:
        count += 1

print("Total amount of zeroes: {0}".format(count))
