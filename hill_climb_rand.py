import random
from utils import neighbors_with_values, cut_value

def hill_climbing_random(n, edges, start_partition):
    current = start_partition
    current_value = cut_value(n, edges, current)

    while True:
        better_neighbors = [
            (val, neigh)
            for neigh, val in neighbors_with_values(n, edges, current)
            if val > current_value
        ]

        if not better_neighbors:
            break

        best_val, best_neigh = random.choice(better_neighbors)
        current, current_value = best_neigh, best_val

    return current_value, current
