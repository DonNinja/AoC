import math


class Location:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._connection = None

    def __sub__(self, other):
        xDist = (self.x - other.x) ** 2
        yDist = (self.y - other.y) ** 2
        zDist = (self.z - other.z) ** 2
        return math.sqrt(xDist + yDist + zDist)

    def __str__(self):
        return "X: {0}, Y: {1}, Z: {2}".format(self.x, self.y, self.z)
    
    def isConnected(self):
        return self._connection != None


file = open("AoC-2025\\Day-8\\testinput.txt", "r")  

results: int = 0

data = file.readlines()

file.close()

pointArray: list[Location] = []

circuitArray = []

for line in data:
    x, y, z = line.strip().split(",")
    
    point = Location(int(x), int(y), int(z))
    pointArray.append(point)

while len(pointArray) > 0:
    point = pointArray(0)
    
    pass

print(results)