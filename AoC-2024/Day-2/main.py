from enum import Enum


class Direction(Enum):
    Static = 0
    Ascending = 1
    Descending = 2


data = open("AoC-2024/Day-2/input", "r")
results = 0

def lineCheck(line, dampen=0):
    direction = Direction.Static
    dampen = dampen - 1

    nums = [int(x) for x in line]

    for i in range(1, len(nums)):
        prevNumber = nums[i - 1]
        currNumber = nums[i]
        if direction == Direction.Static:
            direction = (
                Direction.Ascending if prevNumber < currNumber else Direction.Descending
            )
        if (
            direction == Direction.Ascending
            and prevNumber > currNumber
            or direction == Direction.Descending
            and prevNumber < currNumber
        ):
            if dampen > -1:
                for j in range(0, len(nums)):
                    newNums = nums[0:j] + nums[j + 1 :]
                    if lineCheck(newNums, dampen):
                        return True
            return False

        diff = abs(prevNumber - currNumber)

        if diff > 3 or diff < 1:
            if dampen > -1:
                for j in range(0, len(nums)):
                    newNums = nums[0:j] + nums[j + 1 :]
                    if lineCheck(newNums, dampen):
                        return True
            return False

    return True


for line in data:
    if lineCheck(line.strip().split(" "), 1):

        results += 1
    else:
        # print("Line {0} is unsafe".format(line.strip()))
        pass

print(results)
