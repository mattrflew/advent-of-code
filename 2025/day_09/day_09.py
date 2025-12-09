# https://adventofcode.com/2025/day/8
import numpy as np

# --------------------
# Part 1
# --------------------
# Read input
data = np.loadtxt("input.txt", delimiter=',', dtype=int)
m,n = data.shape

largest_area = -np.inf
for i in range(m-1):
    for j in range(m-1-i):
        x1 = data[i,:].astype(float)
        x2 = data[j,:].astype(float)
        area = (abs(x1[0] - x2[0]) + 1) * (abs(x1[1] - x2[1]) + 1) 
        if area > largest_area:
            largest_area = area

print(f"Part 1: {int(largest_area)}")

# --------------------
# Part 2
# --------------------
def build_boundary(vertices):
    '''
    From vertices, return array of indices of polygon boundary
    '''
    m,_ = vertices.shape
    
    boundary = []
    for i in range(m):
        if i == (m-1):
            x1 = vertices[i,:]
            x2 = vertices[0,:]
        else:
            x1 = vertices[i,:]
            x2 = vertices[i+1,:]
        
        delta = x2-x1
        
        if delta[0] > 0:
            for j in range(1,delta[0]):
                boundary.append([x1[0]+j, x1[1]])
        elif delta[0] < 0:
            for j in range(-1, delta[0], -1):
                boundary.append([x1[0]+j, x1[1]])
        elif delta[1] > 0:
            for j in range(1,delta[1]):
                boundary.append([x1[0], x1[1]+j])
        elif delta[1] < 0:
            for j in range(-1,delta[1], -1):
                boundary.append([x1[0], x1[1]+j])
                
    boundary = np.array(boundary)
    
    return np.concatenate((boundary, vertices))

# Read input
data = np.loadtxt("input.txt", delimiter=',', dtype=int)
m,n = data.shape

vertices = data.astype(np.int64)
perimeter = build_boundary(data)

# Split perimeter into components
perim_x = perimeter[:, 0]
perim_y = perimeter[:, 1]

largest_area = -np.inf
for i in range(m - 1):
    for j in range(m - 1 - i):
        [x1, y1] = vertices[i]
        [x2, y2] = vertices[j + i + 1]

        # Area of rectangle
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        
        # Skip if not better than best
        if area <= largest_area:
            continue
        
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        invalid = False
        for (px, py) in perimeter:
            inside = (perim_x > min_x) & (perim_x < max_x) & (perim_y > min_y) & (perim_y < max_y)
            invalid = inside.any()
            break
        
        # Update best
        if not invalid:
            largest_area = area

print(f"Part 2: {largest_area}")