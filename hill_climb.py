from utils import neighbors_with_values, cut_value, neighbors

def hill_climbing(n, edges, start_partition):
    current = start_partition
    current_value = cut_value(n, edges, current)

    while True:
        neighbor_values = list(neighbors_with_values(n, edges, current))

        best_val = 0
        best_neigh = None

        for partition, value in neighbor_values:
            if value > best_val:
                best_val = value
                best_neigh = partition

        if best_val <= current_value:
            break

        current = best_neigh
        current_value = best_val

    return current_value, current

