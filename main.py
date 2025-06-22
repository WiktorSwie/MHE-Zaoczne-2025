import sys
from utils import read_graph, cut_value, neighbors, random_partition
from maxcut_fullsearch import full_search
from hill_climb import hill_climbing
from hill_climb_rand import hill_climbing_random
from taboo import taboo_cut

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
else:
    print("Nieznany algorytm:", algo)
    sys.exit(1)

print("Cut value:", val)
print("Split:", part)
