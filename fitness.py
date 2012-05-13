import math
import random
import numpy
from treegen import execute_tree

__author__ = 'inc0'

def target_func(x, y):
    return math.pow(x, 4) + math.sqrt(y)

data_input = [(random.random(), random.randint(1, 50)) for i in range(50)]
data_output = [target_func(i[0], i[1]) for i in data_input]
target_io = zip(data_input, data_output)

arg_list = ["x", "y"]
def calculate_fitness(tree):
    fitness = 0
    for io in target_io:
        args = {}
        for i in range(len(io[0])):
            args[arg_list[i]] = io[0][i]
        expected_return = io[1]
        try:
            ret = execute_tree(tree, args)
        except:
            ret = 9999
        fit = abs( (expected_return - ret) / expected_return)
        fitness += abs(fit)
    return fitness

