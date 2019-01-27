"""
Code taken from the shared directory by Professor Adam Purtee

This class implements functions of a priority queue
Priority queue is used for Dijshitra's algorithm
"""


class PQ:
    __slots__ = 'contents'

    def __init__(self):
        self.contents = {}

    def add(self, vertex, cost):
        self.contents[vertex] = cost

    def pop(self):
        cost = None
        result = None
        for v, c in self.contents.items():
            if cost is None or c < cost:
                cost = c
                result = v
        del self.contents[result]
        return result, cost

    def decrease(self, vertex, cost):
        self.contents[vertex] = cost

    def empty(self):
        return len(self.contents) == 0
