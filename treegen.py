from pprint import pprint
import random
from functions import func_list
#from pygraph.classes.graph import graph
#from pygraph.readwrite.dot import write
#import gv

__author__ = 'inc0'

class Node:
    def init(self):
        self.edges = []
        self.func = None

    def append(self, node):
        for e in range(len(self.edges)):
            if random.random() > 0.8:
                self.edges[e] = node
                return
            elif isinstance(e, Node):
                e.append(node)
            else:
                continue
        return True

"""
    def display(self, gr = None, nodes = [], this_id = False):
        root = False
        if not gr:
            gr = graph()
            root = True
            gr.add_nodes([self.func.symbol + " [1]"])
            nodes.append(self.func.symbol)
            this_id = self.func.symbol + " [1]"

        for edge in self.edges:
            if isinstance(edge, Node):
                nodes.append(edge.func.symbol)
                edge_id = edge.func.symbol + " [%s]" % nodes.count(edge.func.symbol)
                gr.add_nodes([edge_id])
                gr.add_edge([edge_id, this_id])
                edge.display(gr, nodes, edge_id)
            else:
                nodes.append(edge)
                edge_id = str(edge) + " [%s]" % nodes.count(edge)
                gr.add_nodes([edge_id])
                gr.add_edge([this_id, edge_id])

        if root:
            dot = write(gr)
            gvv = gv.readstring(dot)
            gv.layout(gvv,'dot')
            gv.render(gvv,'png','tree.png')
"""

def generate_random_tree(max_depth, arg_list, depth = 0):
    if depth != 0 and (max_depth == 0 or depth == max_depth or random.random() > 0.7 ):
        if random.random() > 0.5:
            return random.choice(arg_list)
        else:
            return random.random()
    else:
        depth += 1
        func = random.choice(func_list)
        node = Node()
        node.func = func
        node.edges = [generate_random_tree(max_depth, arg_list, depth) for i in range(func.num_args)]
        return node

def execute_tree(tree, args):
    if isinstance(tree, Node):
        args = [execute_tree(node, args) for node in tree.edges]
        return tree.func(*args)
    elif type(tree) == type(""):
        return args[tree]
    else:
        return tree