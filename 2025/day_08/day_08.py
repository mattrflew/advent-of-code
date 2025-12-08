# https://adventofcode.com/2025/day/8

# --------------------
# Part 1
# --------------------
import numpy as np
import math

data = np.loadtxt("input.txt", delimiter=',', dtype=int)

m,_ = data.shape
distances = np.zeros((m,m))

# Compute all distances
for i in range(m):
    for j in range(m):
        if i == j:
            distances[i,j] = np.inf
        else:
            distances[i,j] = np.linalg.norm(data[i] - data[j])

def add_to_circuits(circuits, idxs):
    a, b = idxs

    # Find which circuit each index belongs to, if any
    circuit_a = None
    circuit_b = None

    for key, nodes in circuits.items():
        if a in nodes:
            circuit_a = key
        if b in nodes:
            circuit_b = key

    # Neither in any circuit -> create new circuit
    if circuit_a is None and circuit_b is None:
        new_key = max(circuits, default=-1) + 1
        circuits[new_key] = {a, b}

    # a in circuit, b not -> append b to circuit_a
    elif circuit_a is not None and circuit_b is None:
        circuits[circuit_a].add(b)

    # b in circuit, a not -> add a to circuit_b
    elif circuit_a is None and circuit_b is not None:
        circuits[circuit_b].add(a)

    # Both in different circuits -> merge them
    elif circuit_a != circuit_b:
        circuits[circuit_a] |= circuits[circuit_b]
        del circuits[circuit_b]

    # Both in same circuit -> Do nothing
    else:
        pass
    return circuits

circuits = {}
for i in range(len(data)):
    # Find shortest distance
    idxs = np.unravel_index(distances.argmin(), distances.shape)
    circuits = add_to_circuits(circuits, idxs)
    
    # Set used indices to inf 
    distances[idxs] = np.inf
    distances[idxs[::-1]] = np.inf

# Find the longest three circuits
circuits_lengths = [len(circuits[key]) for key in circuits]
longest_3 = np.sort(circuits_lengths)[::-1][:3]

result = math.prod(longest_3)
print(f"Part 1: {result}")

# --------------------
# Part 2
# --------------------

data = np.loadtxt("input.txt", delimiter=',', dtype=int)
m,_ = data.shape

# Compute all distances
distances = np.zeros((m,m))
for i in range(m):
    for j in range(m):
        if i == j:
            distances[i,j] = np.inf
        else:
            distances[i,j] = np.linalg.norm(data[i] - data[j])

circuits = {}
one_circuit = False

# Continue joining circuits until one chain is created
while not one_circuit:
    # Find shortest distance
    idxs = np.unravel_index(distances.argmin(), distances.shape)
    circuits = add_to_circuits(circuits, idxs)    
    
    # Set used indices to inf 
    distances[idxs] = np.inf
    distances[idxs[::-1]] = np.inf
    
    # If all indices are present in one chain, stop
    if len(circuits.keys()) == 1:
        k = list(circuits.keys())[0]
        if all(x in circuits[k] for x in list(range(len(data)))):
            one_circuit = True

# Find the last two circuit boxes to be connected
x1, x2 = data[idxs[0]][0], data[idxs[1]][0]

# Convert to floats to avoid memory error
print(f"Part 2: {int(float(x1)*float(x2))}")