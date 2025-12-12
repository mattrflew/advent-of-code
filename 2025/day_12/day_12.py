# https://adventofcode.com/2025/day/12

# --------------------
# Part 1
# --------------------
import re
import numpy as np

def configure_present_shape(shape):
    new = []
    for l in shape:
        a = l[0].replace("#", '1').replace(".", '0')
        a = [int(ch) for ch in a]
        new.append(a)
    
    new = np.array(new)
    area = np.sum(new)
    return new, area

def get_presents(data):
    present_idx_pattern = r"\d:"
    pattern_size = 3
    pattern_start_idx = []

    presents = {}
    for i,line in enumerate(data):
        if line: 
            test = line[0]
            if re.match(present_idx_pattern, test):
                pattern_start_idx.append(i)
                
                key = int(test[0])
                shape = data[i+1:i+pattern_size+1]
                shape, area = configure_present_shape(shape)
                
                if key not in presents.keys():
                    presents[key] = {}
                    presents[key]['shape'] = shape
                    presents[key]['area'] = area
    return presents, pattern_start_idx

def get_regions(regions_input):
    regions = {}

    for i,r in enumerate(regions_input):
        size_input = r[0]
        present_numbers = r[1:]
        size_vals = size_input[:-1].split('x')
        size_vals = [int(s) for s in size_vals]
        
        if i not in regions.keys():
            regions[i] = {}
            regions[i]['size'] = size_vals
            regions[i]['area'] = size_vals[0]*size_vals[1]
            regions[i]['presents'] = [int(s) for s in present_numbers]
            regions[i]['n_presents'] = sum(regions[i]['presents'])
            
    return regions

def read_input(fpath="input.txt"):
    with open(fpath, "r") as f:
        data = [a.split() for a in f.readlines()]
    
    presents, pattern_start_idx = get_presents(data)
    idx = pattern_start_idx[-1]
    regions_input = data[idx+5:]
    
    regions = get_regions(regions_input)

    return presents, regions

def is_valid_region(region, presents):
    m,n = region['size']
    n_presents_fit = (m // 3) * (n // 3)

    occupied_area = 0
    for i,p in enumerate(region['presents']):
        occupied_area += presents[i]['area']*p
        
    # Check if the number of 3x3 grid presents can simply fit in region 
    if region['n_presents'] <= n_presents_fit:
        return True
    
    # Check if the area of the presents is greater than available area in region 
    elif occupied_area > region['area']:
        return False
    
    # Else, need to manipulate the shape
    else:
        assert False

# Read input
presents, regions = read_input()

cnt = 0
for key, region in regions.items():
    cnt += is_valid_region(region, presents)

print(f"Part 1: {cnt}")

# --------------------
# Part 2
# --------------------
print("Merry Christmas!")