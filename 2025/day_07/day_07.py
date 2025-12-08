# https://adventofcode.com/2025/day/7

# --------------------
# Part 1
# --------------------

# Read input
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

# Replace starting location with beam character
data[0] = data[0].replace('S', '|')
grid = [[c for c in data[i]] for i in range(len(data))]

m,n = len(grid), len(grid[0])
cnt = 0

# Loop through grid
for i in range(m-1):
    for j in range(n):
        c = grid[i][j]
        
        if c == '.' or c == '^':
            continue
        
        # If splitter encountered, attempt to place beam on left and right
        if grid[i+1][j] == '^':
            cnt += 1
            if grid[i+1][j-1] == '.':
                grid[i+1][j-1] = '|'
            
            if grid[i+1][j+1] == '.':
                grid[i+1][j+1] = '|'

        else:
            # Go straight down
            grid[i+1][j] = '|'

print(f"Part 1: {cnt}")

# --------------------
# Part 2
# --------------------

# Read input
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

# Replace starting location with beam character
data[0] = data[0].replace('S', '|')
grid = [[c for c in data[i]] for i in range(len(data))]

m,n = len(grid), len(grid[0])

# Initialize summing row to count the split combinations
combinations = [0]*n

# Start counter in first row
start_idx = data[0].find('|')
combinations[start_idx] = 1

# Loop through rest of grid
for i in range(1,m-1):
    for j in range(n):
        
        # If splitter encountered, add the number of paths at its location to the left and right
        if grid[i+1][j] == '^':
            combinations[j-1] +=  combinations[j]
            combinations[j+1] +=  combinations[j]
            combinations[j] =  0

# Sum to get the total number of path combinations 
print(f"Part 1: {sum(combinations)}")