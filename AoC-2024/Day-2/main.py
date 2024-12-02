data = open("AoC-2024/Day-2/testinput", "r")

for line in data:
    nums = line.strip().split(" ")
    nums = [int(x) for x in nums]
    print(nums)