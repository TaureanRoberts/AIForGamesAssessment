from node_class import Node
from vector2_class import Vector2
class Graph(object):
    def __init__(self, dims):
        self.nodes = []
        self.dimension = dims

    #Prototype: def make_nodes(self)
    #Descripton: Populates the graph with nodes
    #Arguements: Takes in a arguement of self
    #PreCondition: takes the size of the grid
    #PostCondition: Assigns each node a guid while the nodes are being made
    #Protection Level: Public
    def make_nodes(self):
        '''Make a search space for the nodes'''
        guid = 0
        for i in range(0, self.dimension.x_pos):
            for j in range(0, self.dimension.y_pos):
                _node = Node(Vector2(i, j), guid)
                guid = guid + 1
                self.nodes.append(_node)

    #Prototype: def find_neighbors(self, guid)
    #Descripton: Finds the neighbors
    #Arguements: takes in a global unique identifier
    #PreCondition: takes the current node/guid and puts it against the graph to move through
    #PostCondition: Returns the list of guids that border the current node
    #Protection Level: Public
    def find_neighbors(self, guid):
        '''Finds the neighbors by getting their guid to give position'''
        top = guid - self.dimension.x_pos  # Top Node
        bot = guid + self.dimension.x_pos  # Bottom Node
        left = guid - 1  # Left Node
        right = guid + 1  # Right Node
        topl = top + 1  # Top Left node
        topr = top - 1  # Top Right node
        botl = bot + 1  # Bottom Left node
        botr = bot - 1  # Bottom Right node
        total_pos = [top, bot, left, right, topl, topr, botl, botr]
        neighbors = []
        for node in self.nodes:
            if total_pos.__contains__(node.guid):
                neighbors.append(node)
        return neighbors

    #Prototype: def get_neighbors(self, neighbors)
    #Descripton: Gets the positon of neighbor by using vector coordinated
    #Arguements: self and the arguement of a graph is used
    #PreCondition: uses the current positions vectors and add/subtracts to get each corner
    #PostCondition: gives the nodes a list of nodes that 
    #Protection Level: Public
    def get_neighbors(self, graph):
        '''Gets the position of neighbor by x and y positions'''
        positions = []
        positions.append(graph.position + Vector2(1, 0)) #right
        positions.append(graph.position + Vector2(-1, 0)) #left
        positions.append(graph.position + Vector2(0, 1)) #top
        positions.append(graph.position + Vector2(0, -1)) #bot
        positions.append(graph.position + Vector2(1, 1)) #top right
        positions.append(graph.position + Vector2(-1, 1)) #top left
        positions.append(graph.position + Vector2(1, -1)) #bot right
        positions.append(graph.position + Vector2(-1, -1)) #bot left
        neighbors = []
        for pos in positions:
            for graph in self.nodes:
                if graph.position == pos:
                    neighbors.append(graph)
        return neighbors
