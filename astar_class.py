from node_class import Node
from vector2_class import Vector2
from graph_class import Graph
import math

    #Prototype: def finding_neighbors(pos, search)
    #Descripton: Finds the neighbors using vector position and uses a searchspace
    #PreCondition: Uses a list of neighbors that are adjacent to the current position
    #PostCondition: Returns the list of neighbors that meet the conditions
    #Protection Level: Public
def finding_neighbors(pos, search):
    '''Finds the neighbors using vector position and uses a searchspace'''
    nays = []
    nays.append(pos + Vector2(-1, 1)) #Top Left
    nays.append(pos + Vector2(0, 1)) #Top
    nays.append(pos + Vector2(1, 1)) #Top Right
    nays.append(pos + Vector2(-1, 0)) #Left
    nays.append(pos + Vector2(1, 0)) # Right
    nays.append(pos + Vector2(-1, -1)) # Bot Left
    nays.append(pos + Vector2(0, -1)) # bot
    nays.append(pos + Vector2(1, -1)) # bot right
    neighbors = []
    for nay in nays:
        for node in search:
            if node.position == nay:
                neighbors.append(node)
    return neighbors

    #Prototype: def algorithm(start_node, goal_node, searchspace)
    #Descripton: The core function for the a-star algorithm
    #PreCondition: Takes in two lists, a open and closed list that take the nodes that are being traversed
    #PostCondition: Returns the list nodes that are in in both lists that has been traversed
    #Protection Level: Public
def algorithm(start_node, goal_node, searchspace):
    '''The a-star algorithm'''
    open_list = []
    closed_list = []
    current_node = start_node
    # 1. Add the starting square (or node) to the open list
    open_list.append(current_node)
    # 2. Loop as long as the open list is not empty
    while open_list:
        # 2.1 Look for the lowest fscore in the open list
        open_list.sort(key=lambda node: node.f_score)
        current_node = open_list[0]
        open_list.remove(current_node)
        # 2.2 Add the current node to the closed list
        closed_list.append(current_node)
        # Extra: if the closed node is in the closed list then break
        if closed_list.__contains__(goal_node):
            current = goal_node
            path = []
            while current is not None:
                path.append(current) #appends current to the path
                current = current.parent #current gets assigned the
            return path
        # 2.3 Find the neighbors of the current node and put them in the open list
        nays = finding_neighbors(current_node.position, searchspace)
        # 2.4 Loop through all the neighbors of the current Node
        for node in nays:
            # 2.4.1 If not traversable or in the closed list
            if closed_list.__contains__(node) or node.traversable == False:
                # Ignore it
                continue
            # 2.4.2 If not in the open list
            if node not in open_list:
                # add to the open list and calc h, g, f scores
                open_list.append(node)
            node.calculate_g_score(current_node)
            node.calculate_h_score(goal_node)
            node.calculate_f_score()

def main():
    grid = Graph(Vector2(7, 7)) #Graph size
    grid.make_nodes() #makes nodes 
    grid.nodes[23].can_traverse = False #wall 1
    grid.nodes[24].can_traverse = False #wall 2
    grid.nodes[25].can_traverse = False #wall 3
    s = grid.nodes[10] #starting node
    g = grid.nodes[38] #goal node
    p = algorithm(s, g, grid) # astar where the start, goal, and graph are taken in

main()
