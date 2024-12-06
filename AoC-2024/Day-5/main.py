import re

data = open("AoC-2024/Day-5/testinput", "r")

orderMap = {}

results = 0

for line in data:
    line = line.strip()
    if re.search(r"\d+\|\d+", line):
        nums = line.split("|")
        if (orderMap.get(nums[1])):
            orderMap[nums[0]] = orderMap[nums[1]]

print(results)

data.close()