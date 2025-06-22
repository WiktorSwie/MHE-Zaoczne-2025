import sys
from utils import read_graph, cut_value, neighbors, random_partition
from maxcut_fullsearch import full_search
from hill_climb import hill_climbing
from hill_climb_rand import hill_climbing_random
from taboo import taboo_cut
from genetic import genetic_algorithm

path = sys.argv[1]
algo = sys.argv[2]

taboo_size = 10

if algo == "taboo":
    if len(sys.argv) >= 4:
        try:
            taboo_size = int(sys.argv[3])
        except ValueError:
            print("taboo_size musi być liczbą całkowitą.")
            sys.exit(1)

n, edges = read_graph(path)
start_partition = random_partition(n)

if algo == "full_search":
    val, part = full_search(n, edges)
elif algo == "hill":
    val, part = hill_climbing(n, edges, start_partition)
elif algo == "hill_rand":
    val, part = hill_climbing_random(n, edges, start_partition)
elif algo == "taboo":
    val, part = taboo_cut(n, edges, start_partition, taboo_size=taboo_size)

elif algo == "genetic":
    try:
        crossover = sys.argv[3]  # 'one_point' lub 'uniform'
        mutation = sys.argv[4]  # 'flip_bit' lub 'swap_bits'
        stop = sys.argv[5]  # 'max_gen' lub 'no_improve'
        pop_size = int(sys.argv[6])
        mutation_rate = float(sys.argv[7])

        val, part = genetic_algorithm(n, edges,
                                      population_size=pop_size,
                                      crossover_method=crossover,
                                      mutation_method=mutation,
                                      stop_condition=stop,
                                      max_generations=100,
                                      max_no_improvement=20,
                                      mutation_rate=mutation_rate)

    except IndexError:
        print("Użycie:")
        print("python main.py <plik> genetic <crossover> <mutation> <stop_cond> <pop_size> <mutation_rate>")
        sys.exit(1)
else:
    print("Nieznany algorytm:", algo)
    sys.exit(1)

print("Cut value:", val)
print("Split:", part)
