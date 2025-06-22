from utils import neighbors
from utils import cut_value


def hill_climbing(n, edges, start_partition):
    current = start_partition
    current_value = cut_value(n, edges, current)

    while True:
        neighbor_values = []
        for neigh in neighbors(current):
            val = cut_value(n, edges, neigh)
            neighbor_values.append((val, neigh))

        best_val, best_neigh = max(neighbor_values, key=lambda x: x[0])

        if best_val <= current_value:
            break

        current, current_value = best_neigh, best_val

    return current_value, current
