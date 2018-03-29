from astar_class import algorithm
from graph_class import Graph
from vector2_class import Vector2
from node_class import Node

def main():
    '''Displays the algorithm when ran'''
    grid = Graph(Vector2(7, 7)) #Graph size
    grid.make_nodes() #makes nodes 
    grid.nodes[23].can_traverse = False #wall 1
    grid.nodes[24].can_traverse = False #wall 2
    grid.nodes[25].can_traverse = False #wall 3
    s = grid.nodes[10] #starting node
    g = grid.nodes[38] #goal node
    p = algorithm(s, g, grid) # astar where the start, goal, and graph are taken in

main()
