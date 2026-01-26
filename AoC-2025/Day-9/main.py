file = open("AoC-2025\\Day-9\\input.txt", "r")

results: int = 0

data = file.readlines()

file.close()

maxArea = 0

for i in range(len(data)):
    line = data[i]
    
    x, y = line.strip().split(",")
    x, y = int(x), int(y)
    
    for n in range(i + 1, len(data)):
        nLine = data[n]
        nX, nY = nLine.strip().split(",")
        nX, nY = int(nX), int(nY)
        
        area = abs((x - nX + 1) * (y - nY + 1))
        
        if area > maxArea:
            maxArea = area
        
print(maxArea)