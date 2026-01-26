class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xPoint = None
        self.yPoint = None
    
    def isInLoop(self, other) -> bool:
        return False
    

file = open("AoC-2025\\Day-9\\input.txt", "r")

results: int = 0

data = file.readlines()

file.close()

maxArea = 0

# for i in range(len(data)):
#     line = data[i]

for i in range(len(data)):
    line = data[i]
    
    x, y = line.strip().split(",")
    x, y = int(x), int(y)
    
    for n in range(i + 1, len(data)):
        isValid = False
        nLine = data[n]
        if not isValid:
            continue
        nX, nY = nLine.strip().split(",")
        nX, nY = int(nX), int(nY)
        
        area = abs((x - nX + 1) * (y - nY + 1))
        
        if area > maxArea:
            maxArea = area

print(maxArea)