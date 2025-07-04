import itertools
from utils import cut_value

def full_search(n, edges):
    best_value = -1
    best_partition = None

    for bits in itertools.product([0, 1], repeat=n):
        value = cut_value(n, edges, bits)
        if value > best_value:
            best_value = value
            best_partition = bits

            print("Cut value:", best_value)
            print("Split:", best_partition)

    return best_value, best_partition
