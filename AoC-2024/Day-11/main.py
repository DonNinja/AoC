data = open("AoC-2024/Day-11/input", "r")


def evolve(stones: list):
    newStones = []

    for stone in stones:
        if stone == "0":
            newStones.append("1")

        elif len(stone) % 2 == 0:
            halfLength = int(len(stone) / 2)
            newStones.append(str(int(stone[:halfLength])))
            newStones.append(str(int(stone[halfLength:])))
            pass

        else:
            newStones.append(str(int(stone) * 2024))

    return newStones


initial = data.readline().strip()

stoneList = initial.split(" ")

for i in range(25):
    stoneList = evolve(stoneList)

    # for stone in stoneList:
    #     print(stone, end=' ')
    # print()
    
print(len(stoneList))


data.close()
