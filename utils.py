import sys
import random

def read_graph(path):
    if path == '-':
        lines = sys.stdin.read().splitlines()
    else:
        with open(path, 'r') as f:
            lines = f.read().splitlines()

    edges = []
    max_node = -1

    for line in lines:
        parts = list(map(int, line.split()))
        u, v = parts[0], parts[1]
        w = parts[2] if len(parts) == 3 else 1
        edges.append((u, v, w))
        max_node = max(max_node, u, v)

    return max_node + 1, edges

def cut_value(n, edges, partition):
    total = 0
    for u, v, w in edges:
        if partition[u] != partition[v]:
            total += w
    return total

def neighbors(partition):
    for i in range(len(partition)):
        new_partition = partition.copy()
        new_partition[i] = 1 - new_partition[i]
        yield new_partition