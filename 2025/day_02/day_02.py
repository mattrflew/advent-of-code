# https://adventofcode.com/2025/day/2
import csv
import re

# Read input
with open("input.txt", "r") as f:
    rdr = csv.reader(f)
    rows = [[y.strip() for y in x] for x in rdr]
IDRanges = [x for y in rows for x in y]

# --------------------
# Part 1
# --------------------
invalidIDs = []

# Loop through each number in each range
for IDRange in IDRanges:
    first, last = IDRange.split("-")
    firstInt, lastInt = int(first), int(last)
    for i in range(firstInt, lastInt+1):
        # 
        s = str(i)
        nDigits = len(str(abs(i)))
        # Only continue if length is an even number
        if (nDigits % 2) == 0:
            nSplit = nDigits // 2
            pattern = s[:nSplit]
            remainder = s[nSplit:]
            
            if pattern == remainder:
                invalidIDs.append(i)

print(f"Part 1: {sum(invalidIDs)}")

# --------------------
# Part 2
# --------------------
invalidIDs = []

# Loop through each number in each range
for IDRange in IDRanges:
    first, last = IDRange.split("-")
    firstInt, lastInt = int(first), int(last)
    for i in range(firstInt, lastInt+1):
        s = str(i)
        L = len(s)
        
        for length in range(1, L//2 + 1):
            if L % length != 0:
                continue
            
            # How many repititions
            reps = L // length
            if reps < 2:
                continue
            
            # Build repeated sequence and see if matches number
            seq = s[:length]
            if seq*reps == s:
                invalidIDs.append(i)
                break # to avoid counting same number more than once

print(f"Part 2: {sum(invalidIDs)}")

# --------------------
# Part 2 (a more elegant regex solution)
# --------------------
invalidIDs = []
pattern = r"(.+)\1+"

for IDRange in IDRanges:
    first, last = IDRange.split("-")
    firstInt, lastInt = int(first), int(last)
    for i in range(firstInt, lastInt+1):
        s = str(i)
        if re.fullmatch(pattern, s):
            invalidIDs.append(i)

print(f"Part 2: {sum(invalidIDs)} (regex solution)")