import math


class Location:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._connection: Location = None

    def __sub__(self, other):
        xDist = (self.x - other.x) ** 2
        yDist = (self.y - other.y) ** 2
        zDist = (self.z - other.z) ** 2
        return math.sqrt(xDist + yDist + zDist)

    def __str__(self):
        return "X: {0}, Y: {1}, Z: {2}".format(self.x, self.y, self.z)

    def connect(self, other):
        self._connection = other

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

    currPoint = Location(int(x), int(y), int(z))
    pointArray.append(currPoint)

for point in pointArray:
    
    pass

for i in range(len(circuitArray)):
    print("CIRCUIT {0}".format(i))
    for c in circuitArray[i]:
        print(c)
    pass


# print(results)
