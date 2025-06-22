import random

from utils import neighbors
from utils import cut_value


def hill_climbing_random(n, edges, start_partition):
    current = start_partition
    current_value = cut_value(n, edges, current)

    while True:
        better_neighbors = []
        for neigh in neighbors(current):
            val = cut_value(n, edges, neigh)
            if val > current_value:
                better_neighbors.append((val, neigh))
        if not better_neighbors:
            break

        best_val, best_neigh = random.choice(better_neighbors)
        current, current_value = best_neigh, best_val

    return current_value, current