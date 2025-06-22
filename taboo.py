from utils import neighbors, cut_value


def taboo_cut(n, edges, start_partition, taboo_size=10, max_iter=1000):
    current = start_partition
    current_value = cut_value(n, edges, current)

    best = current
    best_value = current_value

    tabu_list = []
    history = []

    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1

        neighs = list(neighbors(current))

        candidate_neighbors = []
        for neigh in neighs:
            if neigh not in tabu_list:
                val = cut_value(n, edges, neigh)
                candidate_neighbors.append((val, neigh))

        if not candidate_neighbors:
            if not history:
                break
            current, current_value = history.pop()
            continue

        candidate_neighbors.sort(key=lambda x: x[0], reverse=True)
        best_val, best_neigh = candidate_neighbors[0]

        history.append((current, current_value))

        current = best_neigh
        current_value = best_val

        tabu_list.append(current)
        if taboo_size and len(tabu_list) > taboo_size:
            tabu_list.pop(0)

        if current_value > best_value:
            best = current
            best_value = current_value

    return best_value, best
