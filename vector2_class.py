import math
class Vector2(object):
    
    #Prototype: def __init__(self, rhs, lhs)
    #Description: Uses the vectors to give positions and size to be set and adjusted
    #PreCondition: Takes the takes the two axis
    #PostCondition: Assigns the x axis the the left hand side and the y axis to the right hand side
    #ProtectionLevel: Public
    def __init__(self, lhs, rhs):
        self.x_pos = lhs
        self.y_pos = rhs

    #Prototype: def __add__(self, other)
    #Descripton: overloads the addidion opperator
    #PreCondition: the node position and adds it to other
    #PostCondition:  Returns sum of the vector 
    #Protection Level: Public
    def __add__(self, other):
        '''Overloads the addition operator'''
        new_vect2 = Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
        return new_vect2

    #Prototype: def __sub__(self, other)
    #Descripton: Overloads the subtraction operators
    #PreCondition: takes the position and subtracts it to a node
    #PostCondition: Returns the new position
    #Protection Level: Public
    def __sub__(self, other):
        '''Overloads the subtraction funtions'''
        new_vect2 = Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)
        return new_vect2

    #Prototype: def __mul__(self, other)
    #Descripton: scales the points of the vectors
    #PreCondition: takes the current position and scales the values of the current node
    #PostCondition: returns a scaled version of the current node
    #Protection Level: Public
    def __mul__(self, other):
        '''Scales the vectors'''
        new_vect2 = Vector2(self.x_pos * other, self.y_pos *other)
        return new_vect2

    #Prototype: def dot(self, other)
    #Descripton: Overloads the dot operator
    #PreCondition: takes in two positions
    #PostCondition: returns the flow between two angles
    #Protection Level: Public
    def dot(self, other):
        '''Dot operator overloader'''
        spot = self.x_pos * other.x_pos + self.y_pos * other.y_pos
        return spot

    #Prototype: def magnitude(self)
    #Descripton: gets the magnitude of the vector
    #PreCondition: Use pyhagoras theorem with the current positions magnitude
    #PostCondition: Returns the magnitude of the current position
    #Protection Level: Public
    def magnitude(self):
        '''Gets the magnitude of the vector'''
        magn = math.sqrt(self.x_pos * self.x_pos + self.y_pos * self.y_pos)
        return magn

    #Prototype: def normalize(self)
    #Descripton: Normalizes the magnitude of the Vector 
    #PreCondition: Takes the current x and y and divides it against the magnitude of the current position
    #PostCondition: Returns a vector with a normalized vector
    #Protection Level: Public
    def normalize(self):
        '''Normalizes the magnitude of the vector'''
        mag = self.magnitude()
        norm = Vector2(self.x_pos / mag, self.y_pos / mag)
        return norm

    #Prototype: def __eq__(self, other)
    #Descripton: Overloads the "Equals to" (==) operator
    #PreCondition: Compares one position against "other's" positions
    #PostCondition: Allows the comparison of two vectors 
    #Protection Level: Public
    def __eq__(self, other):
        '''Overloads the == operator'''
        return (self.x_pos == other.x_pos and self.y_pos == other.y_pos)
        