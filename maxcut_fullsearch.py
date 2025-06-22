import itertools

def calculate_cut_value(edges, partition):
    cut_value = 0
    for u, v, w in edges:
        if partition[u] != partition[v]:
            cut_value += w
    return cut_value

def full_search(n, edges):
    best_value = -1
    best_partition = None

    for bits in itertools.product([0, 1], repeat=n):
        value = calculate_cut_value(edges, bits)
        if value > best_value:
            best_value = value
            best_partition = bits

    return best_value, best_partition