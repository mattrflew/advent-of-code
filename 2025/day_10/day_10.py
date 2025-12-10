# https://adventofcode.com/2025/day/10
import re
import itertools
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

# --------------------
# Part 1
# --------------------
def parse_line(line):
    diagram = line[0][1:-1]
    joltages_str = line[-1][1:-1]
    joltages = [int(a) for a in joltages_str.split(',')]
    
    buttons_str = line[1:-1]
    pattern = r"\((.*?)\)"
    buttons = []
    for b in buttons_str:
        nums_str = re.findall(pattern, b)
        nums_str = nums_str[0].split(',')
        these_buttons = [int(c) for c in nums_str]
        buttons.append(these_buttons)

    return diagram, buttons, joltages

def result_to_diagram(result):
    diagram = list('.'*len(result))
    for i,val in enumerate(result):
        if (val % 2 != 0):
            diagram[i] = '#'

    return "".join(diagram)

def min_presses_part1(diagram, buttons):
    # Extract information
    n_buttons = len(buttons)
    idx = list(range(n_buttons))
    
    n_digits = len(diagram)
    
    # Initialize permutation information
    n_press = 0
    
    # While loop conditional
    solution = False
    
    while not solution:
        # Create list of permutations of button presses
        n_press += 1
        perms = list(itertools.combinations_with_replacement(idx, n_press))
        
        # Loop through all permutations
        for perm in perms:
            # Initialize the result of pressing buttons of the permutation
            result = [0 for _ in range(n_digits)]
            
            # Start pressing the buttons, loop through index of different presses
            for step in perm:
                # Determine which buttons to press
                b = buttons[step]
                for i in b:
                    result[i] += 1
            
            # Compare the result
            result_diagram = result_to_diagram(result)
            
            # Break if result matches the target
            if result_diagram == diagram:
                # print('Solution Found')
                solution = True
                break
    return n_press

# Read input
with open("input.txt", "r") as f:
    data = [a.split() for a in f.readlines()]

total_presses = 0

# Loop through each line
for line in data:    
    # Parse the line
    diagram, buttons, joltages = parse_line(line)
    
    # Determine number of presses to achieve target diagram
    n_press = min_presses_part1(diagram, buttons)
    total_presses += n_press

print(f"Part 1: {total_presses}")

# --------------------
# Part 2
# --------------------
# Far too expensive to attempt the permutation approach.
# Treat as a linear programming problem

def buttons_to_matrix(buttons, joltages):
    m = len(joltages)
    n = len(buttons)

    A = np.zeros((m,n))

    for j,button in enumerate(buttons):
        for i in button:
            A[i, j] = 1
    return A

def min_press_part2(line):
    _, buttons, joltages = parse_line(line)
    
    A = buttons_to_matrix(buttons, joltages)
    b = np.array(joltages)
    _,n = A.shape

    # Want to minimize c^Tx (min sum(x))
    c = np.ones(n)

    # constraints (Ax = b)
    constraints = LinearConstraint(A, b, b)

    # Bounds (x >= 0, no upper bound)
    bounds = Bounds(lb=0, ub=np.inf)

    # Specify the solution must be integers
    integrality = np.ones(n)
    
    # Solve the linear programming problem
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

    return np.ceil(sum(result.x))

# Read input
with open("input.txt", "r") as f:
    data = [a.split() for a in f.readlines()]

total_presses = 0

for i,line in enumerate(data):
    min_presses = min_press_part2(line)
    total_presses += min_presses

print(f"Part 2: {total_presses}")