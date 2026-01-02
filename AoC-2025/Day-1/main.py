data = open("AoC-2025\\Day-1\\input.txt", "r")

dialMax = 100
dialMin = 0

# Current direction of the dial
dialDir = 50

count = 0

for line in data:
    line = line.strip()

    #First letter tells which direction we rotate in
    direction = line[0]
    
    # After that comes the amount of degrees
    rotation = int(line[1:])

    # This finds how many 100 degree revolutions there are and counts them
    amountRevolved = rotation // dialMax
    
    # Offset the amount of revolutions if the dial starts at 0
    if dialDir == 0:
        amountRevolved -= 1

    # Remove the extra rotations
    rotation -= amountRevolved * dialMax

    # If we rotate left, it counts as a negative
    if direction == "L":
        rotation *= -1

    dialDir += rotation

    # Add another revolution if it surpasses 0 or 99
    if dialDir < 0 or dialDir > dialMax:
        # print("Added to revolutions when dialDir is {0}".format(dialDir))
        amountRevolved += 1

    # Find the correct direction the dial should be at
    dialDir = dialDir % dialMax

    count += amountRevolved

    # Add to the count if the dial ends at a 0
    if dialDir == 0:
        count += 1

# print(dialDir)

print("Total amount of zeroes: {0}".format(count))
