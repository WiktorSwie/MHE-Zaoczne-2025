import random
from utils import neighbors_with_values, cut_value

def hill_climbing_random(n, edges, start_partition, iter=20):
    current = start_partition
    current_value = cut_value(n, edges, current)
    cur_iter = 0

    while cur_iter < iter:
        neighbors = [
            (val, neigh)
            for neigh, val in neighbors_with_values(n, edges, current)
        ]

        if not neighbors:
            break

        val, neigh = random.choice(neighbors)
        current, current_value = neigh, val
        cur_iter += 1

    return current_value, current
