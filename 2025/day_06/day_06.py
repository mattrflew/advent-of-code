# https://adventofcode.com/2025/day/6
import numpy as np
from math import prod

# Read input
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

# --------------------
# Part 1
# --------------------
problems = [line.split() for line in data]
problems = np.array(problems)
m,n = problems.shape

def perform_arithmetic(nums, operator):
    if operator == "+":
        total = 0
        for num in nums:
            total += int(num)
    elif operator == "*":
        total = 1
        for num in nums:
            total *= int(num)
    return total

total = 0
for i in range(n):
    problem = problems[:,i]
    nums = problem[:-1]
    operator = problem[-1]
    total += perform_arithmetic(nums, operator)

print(f"Part 1: {total}")


# --------------------
# Part 2
# --------------------
lines = [line.ljust(max(map(len, data))) for line in data]
lines
cols = ("".join(line[i] for line in lines) for i in reversed(range(len(lines[0]))))

total = 0
nums = []

ops = {"*": prod, "+":sum}

for col in cols:
    if not col.strip():
        continue
    
    nums.append(int(col[:-1]))
    
    if op := ops.get(col[-1]):
        total += op(nums)
        nums = []

print(f"Part 2: {total}")