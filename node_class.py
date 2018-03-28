from vector2_class import Vector2
import math
class Node(object):
    def __init__(self, pos, _guid):
        self.guid = _guid
        self.position = pos
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.can_traverse = True

    #Prototype: def calc_g_score(self, node)
    #Description: Calculates the g score of the nodes in the list
    #Arguements: uses self and takes a node as the arguement
    #PreCondition: Takes in a Vector2
    #PostCondition: Gives a value due to the nodes position to the current node
    #Protection Level: Public
    def calc_g_score(self, node):
        '''Calculates the g_score of the nodes in the graph and does tentative_g'''
        if self.position.x_pos == node.position.x_pos and self.position.y_pos == node.position.y_pos:
            return
        if self.parent is None:
            if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
                self.g_score = node.g_score + 10
            else:
                self.g_score = node.g_score + 14
            self.parent = node
        if node.parent is not None:
            tentative = self.g_score
            if self.position.x_pos == node.position.x_pos or self.position.y_pos == node.position.y_pos:
                tentative = node.g_score + 10
            else:
                tentative = node.g_score + 14
            if tentative < self.g_score:
                self.g_score = tentative
                self.parent = node
                return

    #Prototype: calc_h_score(self, node)
    #Description: Calculates the h score or the heuristic for the node
    #Arguements: uses self and  takes a node
    #PreCondition: Takes the current nodes position and use manhattan distance to find the h score
    #PostCondition: gives a the nodes a heuristic for calculation
    #ProtectionLevel: public
    def calc_h_score(self, node):
        self.h_score = (abs(self.position.x_pos - node.position.x_pos) + abs(self.position.y_pos - node.position.y_pos)) * 10

    #Prototype: def calc_fscore(self)
    #Description: Combines the score of the g and h score to find the hscore
    #Arguements: Takes in no arguements other than self
    #PreCondition: Add the results of the g and h scores
    #PostCondition: The total of the two scores gives the f score
    #ProtectionLevel: Public
    def calc_f_score(self):
        self.f_score = self.g_score + self.h_score

    #Prototype: def set_parent 
    #Descripton: Sets the parents of the nodes of the 
    #Arguements: Uses self and Takes a node
    #PreCondition: Checks the nodes and can trace the nodes to the start
    #PostCondition: A list of nodes that allows traceing to the start
    #Protection Level: Public
    def set_parent(self, node):
        '''Checks the nodes parents and can trace node to start'''
        self.parent = node
