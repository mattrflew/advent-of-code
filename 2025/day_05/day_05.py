# https://adventofcode.com/2025/day/5

# Read input
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

split_idx = data.index('')
ranges_raw = data[:split_idx]
IDs = [int(n) for n in data[split_idx+1:]]

# --------------------
# Part 1
# --------------------
ranges_dict = {}
for i,r in enumerate(ranges_raw):
    r_split = r.split("-")
    ranges_dict[i] = {"lower":int(r_split[0]),
                    "upper":int(r_split[1])}

cnt = 0
for ID in IDs:
    for key in ranges_dict:
        if (ID >= ranges_dict[key]["lower"]) and (ID <= ranges_dict[key]["upper"]):
            cnt += 1
            break 
print(f"Part 1: {cnt}")

# --------------------
# Part 2
# --------------------
# Arrange as a list of sets
ranges = []
for r in ranges_raw:
    lower, upper = r.split("-")
    ranges.append((int(lower), int(upper)))

# Sort by lower bound
ranges.sort(key=lambda x: x[0])

merged = []
current_lower, current_upper = ranges[0] 

for lower, upper in ranges[1:]:

    if lower <= current_upper + 1:
        # New lower bound is within range, select the greater upper bound 
        current_upper = max(current_upper, upper)
    else:
        # New range is not already in list, append it
        merged.append((current_lower, current_upper))
        current_lower, current_upper = lower, upper

# append last range
merged.append((current_lower, current_upper))

# Find number of valid IDs in all the ranges
total = sum(u - l + 1 for l, u in merged)
print(f"Part 2: {total}")