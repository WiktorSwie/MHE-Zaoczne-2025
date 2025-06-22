from utils import neighbors_with_values, cut_value, neighbors


def hill_climbing(n, edges, start_partition):
    current = start_partition
    current_value = cut_value(n, edges, current)

    while True:
        neighbor_values = list(neighbors_with_values(n, edges, current))

        best_neigh, best_val = max(neighbor_values, key=lambda x: x[1])

        if best_val <= current_value:
            break

        current, current_value = best_neigh, best_val

    return current_value, current

