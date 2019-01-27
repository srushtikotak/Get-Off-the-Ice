"""
Code taken from the shared directory by Professor Adam Purtee
"""


class Vertex:
    """ 
     Outgoing edges are represented using a dictionary from
     destination vertex to edge weight.  This subsumes the
     adjacency list representation, as we can always get the
     keys from a dictionary.  This has the advantage of
     testing whether one vertex is an edge of another vertex
     in O(1).  Similarly, adding an edge with this representation
     is O(1).
    """    
    __slots__ = ('name', 'outEdges',)

    def __init__(self, name):
        self.name = name
        self.outEdges = {}       # could use set, list, or dictionary.

    def addOutEdge(self, outVertex, cost=1):
        """ :param outVertex: a reference to a Vertex object."""
        self.outEdges[outVertex] = cost

    def hasEdge(self, outVertex):
        return outVertex in self.outEdges

    def neighbors(self):
        return self.outEdges.items()

    def __str__(self):
        result = "<" + str(self.name) + ":"
        first = True
        for vout in self.outEdges:
            if not first:
                result += ", "
            else:
                first = False
            result += str(vout.name)
        result += ">"
        return result
