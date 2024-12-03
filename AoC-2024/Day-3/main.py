"""
    This should be a pretty simple case of a regex, however what pitfalls are created when the 2nd part reveals itself
"""

import re

data = open("AoC-2024/Day-3/input", "r")

results = 0
shouldMult = True

for line in data:

    allRegs = re.finditer(r"(mul\(\d{1,3},\d{1,3}\))|(don\'t\(\))|(do\(\))", line)

    for match in allRegs:
        print(match.group())
        mul = re.search(r"\d{1,3}\,\d{1,3}", match.group())

        if mul:
            if shouldMult:
                nums = [int(x) for x in mul.group().split(",")]

                print(f"MULTIPLYING {nums}")

                results += nums[0] * nums[1]

        else:
            print(f"RESULTS: {results}")
            if re.search(r"do\(\)", match.group()):
                shouldMult = True
            else:
                shouldMult = False

        # nums = re.findall("\d{1,3},\d{1,3}", match.group())[0].split(",")

        # nums = [int(x) for x in nums]

        # results += nums[0] * nums[1]

    # for mul in allRegs:

print(results)
