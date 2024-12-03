'''
    This should be a pretty simple case of a regex, however what pitfalls are created when the 2nd part reveals itself
'''

import re

data = open("AoC-2024/Day-3/input", "r")

results = 0

for line in data:
    allRegs = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    
    for mul in allRegs:
        nums = re.findall("\d{1,3},\d{1,3}", mul)[0].split(",")
        
        nums = [int(x) for x in nums]
        
        results += nums[0] * nums[1]
        pass

print(results)