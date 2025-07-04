import random
from utils import cut_value

def crossover_one_point(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def crossover_uniform(parent1, parent2):
    child1, child2 = [], []
    for g1, g2 in zip(parent1, parent2):
        if random.random() < 0.5:
            child1.append(g1)
            child2.append(g2)
        else:
            child1.append(g2)
            child2.append(g1)
    return child1, child2

def mutation_flip_bit(solution, mutation_rate=0.1):
    return [1 - bit if random.random() < mutation_rate else bit for bit in solution]

def mutation_swap_bits(solution, mutation_rate=0.1):
    mutated = solution.copy()
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(solution)), 2)
        mutated[i], mutated[j] = mutated[j], mutated[i]
    return mutated

def stop_condition_max_gen(max_gen):
    def condition(current_gen, _):
        return current_gen >= max_gen
    return condition

def stop_condition_no_improve(max_no_improve):
    def condition(_, no_improve_count):
        return no_improve_count >= max_no_improve
    return condition

def get_fitness(individual_with_fitness):
    return individual_with_fitness[1]

def tournament_selection(population, fitnesses, tournament_size=3):
    participants = random.sample(list(zip(population, fitnesses)), tournament_size)
    best_individual = max(participants, key=get_fitness)
    return best_individual[0]

def genetic_algorithm(n, edges,
                      population_size=50,
                      crossover_method='one_point',
                      mutation_method='flip_bit',
                      stop_condition='max_gen',
                      max_generations=100,
                      max_no_improvement=20,
                      mutation_rate=0.1):

    crossover_funcs = {
        'one_point': crossover_one_point,
        'uniform': crossover_uniform,
    }

    mutation_funcs = {
        'flip_bit': mutation_flip_bit,
        'swap_bits': mutation_swap_bits,
    }

    stop_conditions = {
        'max_gen': stop_condition_max_gen(max_generations),
        'no_improve': stop_condition_no_improve(max_no_improvement),
    }

    crossover = crossover_funcs[crossover_method]
    mutation = mutation_funcs[mutation_method]
    stop_cond = stop_conditions[stop_condition]

    population = [[random.choice([0, 1]) for _ in range(n)] for _ in range(population_size)]

    best_solution = None
    best_fitness = -float('inf')
    no_improve_count = 0
    generation = 0

    while True:
        generation += 1
        fitnesses = [cut_value(n, edges, ind) for ind in population]

        current_best_fitness = max(fitnesses)
        current_best_sol = population[fitnesses.index(current_best_fitness)]

        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_solution = current_best_sol
            no_improve_count = 0
        else:
            no_improve_count += 1

        if stop_cond(generation, no_improve_count):
            break

        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutation(child1, mutation_rate))
            if len(new_population) < population_size:
                new_population.append(mutation(child2, mutation_rate))

        population = new_population

    return best_fitness, best_solution
