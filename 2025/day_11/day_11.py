# https://adventofcode.com/2025/day/11
import networkx as nx

# --------------------
# Part 1
# --------------------
def define_nodes(data):
    nodes = {}
    idx = -1
    for line in data:
        key = line[0][:-1]
        vals = line[1:]
        
        if key not in nodes.keys():
            idx += 1
            nodes[key] = idx
        
        for val in vals:
            if val not in nodes.keys():
                idx += 1
                nodes[val] = idx
    return nodes

def define_edges(data, nodes):
    edges = []

    for line in data:
        key = line[0][:-1]
        vals = line[1:]
        
        key_idx = nodes[key]
        val_idx = []
        for val in vals:
            val_idx = nodes[val]
            
            edges.append((key_idx, val_idx))
    
    return edges

def define_graph(data):
    nodes = define_nodes(data)
    edges = define_edges(data, nodes)
    
    G = nx.DiGraph()
    n = len(list(nodes.values()))
    G.add_nodes_from(range(n))
    
    G.add_edges_from(edges)
    return G, nodes

# Read input
with open("input.txt", "r") as f:
    data = [a.split() for a in f.readlines()]

# Build Graph
G, nodes = define_graph(data)

# Define source and target
source_node = nodes['you']
target_node = nodes['out']

# Generate all simple paths between source and target
path_generator = nx.all_simple_paths(G, source=source_node, target=target_node)

# Convert the generator to a list
all_paths_list = list(path_generator)

n_paths = len(all_paths_list)

print(f"Part 1: {n_paths}")

# --------------------
# Part 2
# --------------------
# Can't simply reuse the code from Part 1 and filter the paths as the graph is far too big.
# Instead need to go for a counting approach

def count_paths(G, node1, node2):
    '''
    Count the number of directed paths from node1 to node2 using topological sorting
    '''
    # Topological ordering of the nodes.
    order = list(nx.topological_sort(G))

    # dp[u] = number of distinct paths from s to u
    # Initialize all counts to zero.
    dp = {node: 0 for node in G}
    
    # Start node has one trivial path to itself
    dp[node1] = 1

    # Process nodes in topological order
    # When we reach a node u, dp[u] already contains the total number
    # of paths from node1 to u. We add that number to each successor v,
    # because every path to u can be extended to v
    for u in order:
        for v in G.successors(u):
            dp[v] += dp[u]

    # The number of paths from node1 to node2 is now stored in dp[node2]
    return dp[node2]

# Read input
with open("input.txt", "r") as f:
    data = [a.split() for a in f.readlines()]

# Build Graph
G, nodes = define_graph(data)

# Define source and target
source_node = nodes['svr']
target_node = nodes['out']
fft_node = nodes['fft']
dac_node = nodes['dac']

# Compute the number of paths for each segment of interest
n_svr_fft = count_paths(G, source_node, fft_node)
n_svr_dac = count_paths(G, source_node, dac_node)

n_fft_dac = count_paths(G, fft_node, dac_node)
n_dac_fft = count_paths(G, dac_node, fft_node)

n_dac_out = count_paths(G, dac_node, target_node)
n_fft_out = count_paths(G, fft_node, target_node)

# Total paths svr -> out including fft and dac
total = 0

# Case 1: svr -> fft -> dac -> out
if n_fft_dac > 0:
    total += n_svr_fft * n_fft_dac * n_dac_out

# Case 2: svr -> dac -> fft -> out
if n_dac_fft > 0:
    total += n_svr_dac * n_dac_fft * n_fft_out

print(f"Part 2: {total}")