from pprint import pprint
import random

__author__ = 'inc0'
from treegen import generate_random_tree, execute_tree, Node
from fitness import calculate_fitness,arg_list

GENERATION_SIZE = 300
trees = []
for i in range(GENERATION_SIZE):
    tree = generate_random_tree(5, arg_list)
    trees.append(tree)



def get_node(tree):
    if isinstance(tree, Node):
        for e in tree.edges:
            if random.random() < 0.3:
                return e
            else:
                return get_node(e)
            return tree
    return tree

def crossover(father, mother):
    node = get_node(mother)
    father.append(node)
    return mother

fits = []
for t in trees:
    fits.append(calculate_fitness(t))
fits.sort()
print fits[:5]


for i in range(60):
    fits = {}
    for t in trees:
        fit = calculate_fitness(t)
        fits[fit] = t
    keys = fits.keys()
    keys.sort()
    keys = keys[:int(GENERATION_SIZE / 2)]
    trees = []
    for t in keys:
        for i in range(2):
            father = fits[t]
            mother = generate_random_tree(5, arg_list)
            offspring = crossover(father, mother)
            trees.append(offspring)

keys = fits.keys()
keys.sort()
pprint(keys[:10])

print fits[keys[0]]