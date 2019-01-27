"""
Code taken from the shared directory by Professor Adam Purtee
"""

from pq import *
from vertex import *


class Graph:
    __slots__ = 'vertices'  # no need to keep track of edges, because that's stored in the vertices

    def __init__(self):
        self.vertices = {}  # dictionary lets hasVertex be O(1)

    def addVertex(self, name):
        """ :param name: -- a string identifying the vertex """
        if name in self.vertices:
            print("Warning: overwriting vertex", self, "may destroy edges.")
        self.vertices[name] = Vertex(name)

    def hasVertex(self, name):
        """ :param name: -- a string identifying the vertex """
        return name in self.vertices

    def getVertex(self, name):
        """ :param name: -- a string identifying the vertex
            :returns: -- the corresponding Vertex instance """
        if self.hasVertex(name):
            return self.vertices[name]

    def addEdge(self, vid1, vid2, weight=1):
        """:param vid1, vid2: names for vertices when adding edge vid1->vid2.
          :note: vertices not already in the graph will be added."""
        if not self.hasVertex(vid1):
            self.addVertex(vid1)
        if not self.hasVertex(vid2):
            self.addVertex(vid2)

        v1 = self.getVertex(vid1)
        v2 = self.getVertex(vid2)

        v1.addOutEdge(v2, weight)

    def dijkstra(self, sourceName, destName):
        """
           Compute the path through the graph from a sourceName to a destName vertex
           whose sum of edge weights is minimized.
           :param sourceName: the key name of the starting vertex
           :param destName: the key name of the ending vertex
        """
        q = PQ()
        steps = {}
        source = self.getVertex(sourceName)
        dest = self.getVertex(destName)
        costs = {source: 0}
        q.add(source, 0)
        while not q.empty():
            v, c = q.pop()
            if v is dest:
                return unwind(steps, source, dest)
            for n, w in v.outEdges.items():
                if n not in costs:
                    q.add(n, c + w)
                    costs[n] = c + w
                    steps[n] = v
                elif c + w < costs[n]:  # found new or better path to n through v
                    costs[n] = c + w
                    steps[n] = v
                    q.decrease(n, costs[n])
        return None


def unwind(steps, begin, end):
    if begin is end:
        return [begin]
    else:
        return unwind(steps, begin, steps[end]) + [end]

