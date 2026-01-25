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

circuitArray: list[list] = []

for line in data:
    x, y, z = line.strip().split(",")

    currPoint = Location(int(x), int(y), int(z))
    pointArray.append(currPoint)

for point in pointArray:
    closestPoint = (math.inf, None)
    for otherPoint in pointArray:
        if point - otherPoint < closestPoint[0] and otherPoint != point:
            closestPoint = (point - otherPoint, otherPoint)

    foundCircuit = False

    # print("Closest point to {0} is {1}".format(point, closestPoint[1]))
    


for i in range(len(circuitArray)):
    print("CIRCUIT {0} of size {1}".format(i, len(circuitArray[i])))
    for c in circuitArray[i]:
        print(c)
    pass


# print(results)
