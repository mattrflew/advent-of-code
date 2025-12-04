# https://adventofcode.com/2025/day/4
import numpy as np

# Read input
with open("input.txt") as f:
    grid = [line.strip().replace('.', '0').replace('@', '1') for line in f]

grid = np.array([[int(c) for c in row] for row in grid], dtype=int)


def conv2D(grid, kernel):
    m,n = grid.shape
    
    # With padding
    grid_padded = np.zeros((m+2,n+2))
    grid_padded[1:m+1, 1:n+1] = grid
    
    # Initialize
    grid_conv = np.zeros_like(grid)

    # Perform convolution
    for i in range(1,m+1):
        for j in range(1,n+1):
            block = grid_padded[(i-1):(i+2), (j-1):(j+2)]
            grid_conv[i-1,j-1] = np.sum(block*kernel)
    
    return grid_conv

def to_be_removed(grid_conv, grid):
    return np.logical_and((grid_conv < 4), grid)

kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])

# --------------------
# Part 1
# --------------------
grid_p1 = np.copy(grid)

grid_conv = conv2D(grid_p1, kernel)

grid_remove = to_be_removed(grid_conv, grid_p1)

print(f"Part 1: {np.sum(grid_remove)}")

# --------------------
# Part 2
# --------------------
grid_iter = grid
grid_remove = np.zeros_like(grid)

total = 0
removed_count = 1

while removed_count != 0:
    grid_iter[grid_remove==1] = 0
    
    grid_conv = conv2D(grid_iter, kernel)
    
    grid_remove = to_be_removed(grid_conv, grid_iter)
    
    removed_count = np.sum(grid_remove)
    
    total += removed_count

print(f"Part 2: {total}")