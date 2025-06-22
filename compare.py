import time
import psutil
import matplotlib.pyplot as plt
from utils import read_graph, random_partition, cut_value
from hill_climb import hill_climbing
from hill_climb_rand import hill_climbing_random
from taboo import taboo_cut
from genetic import genetic_algorithm

def run_experiment(name, func, args_generator, repeat=30):
    results = []
    for _ in range(repeat):
        args = args_generator()

        process = psutil.Process()
        mem_before = process.memory_info().rss
        cpu_before = time.process_time()

        val, sol = func(*args)

        cpu_after = time.process_time()
        mem_after = process.memory_info().rss

        results.append({
            "value": val,
            "cpu_time": cpu_after - cpu_before,
            "mem_MB": (mem_after - mem_before) / (1024 * 1024),
        })
    return results

def plot_results(all_results, metric, title):
    plt.figure(figsize=(10, 6))
    for method, results in all_results.items():
        values = [r[metric] for r in results]
        x = list(range(1, len(values) + 1))
        plt.plot(x, values, marker='o', label=method)
    plt.title(f"{title} ({metric})")
    plt.xlabel("Powtórzenie")
    plt.ylabel(metric)
    plt.xticks(x)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{title.lower().replace(' ', '_')}_{metric}.png")
    plt.close()

if __name__ == "__main__":

    path = "graph3.txt"
    n, edges = read_graph(path)

    all_results = {}

    all_results["hill"] = run_experiment(
        "hill",
        hill_climbing,
        args_generator=lambda: [n, edges, random_partition(n)],
    )

    all_results["hill_rand"] = run_experiment(
        "hill_rand",
        lambda n, edges: hill_climbing_random(n, edges, random_partition(n)),
        args_generator=lambda: [n, edges]
    )

    all_results["taboo"] = run_experiment(
        "taboo",
        taboo_cut,
        args_generator=lambda: [n, edges, random_partition(n), 7, 500]
    )

    all_results["genetic"] = run_experiment(
        "genetic",
        genetic_algorithm,
        args_generator=lambda: [
            n,
            edges,
            50,  # population_size
            "uniform",  # crossover_method
            "flip_bit",  # mutation_method
            "no_improve",  # stop_condition
            100,  # max_generations
            15,  # max_no_improvement
            0.1  # mutation_rate
        ]
    )

    for metric in ["value", "cpu_time", "mem_MB"]:
        plot_results(all_results, metric, "Porównanie metod")

