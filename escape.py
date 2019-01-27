"""
CSCI-603: LAB 9

This program reads an ice maze from a file and finds paths to get off the ice!!
Authors: Srushti Kotak
         Suchit Nandal
"""

from graph import *


def create_graph(pond_representation, row, col, m, n, g):
    """
    :param pond_representation:
    :param row: row number of the node being tested
    :param col: column number of the node being tested
    :param m: height of the pond
    :param n: width of the pond
    :param g: Graph object
    """
    if pond_representation[row][col] == "*":
        return
    """ Adds edges left to right """
    for i in range(col, m):
        if pond_representation[row][i] == '*':
            if col == i-1:
                break
            src = str(row) + str(col)
            des = str(row) + str(i-1)
            g.addEdge(src, des)
            break
        elif i == m-1:
            if col == m-1:
                break
            src = str(row) + str(col)
            des = str(row) + str(m-1)
            g.addEdge(src, des)
    """ Adds edges top to bottom """
    for i in range(row, n):
        if pond_representation[i][col] == '*':
            if row == i-1:
                break
            src = str(row) + str(col)
            des = str(i-1) + str(col)
            g.addEdge(src, des)
            break
        elif i == n-1:
            if row == n-1:
                break
            src = str(row) + str(col)
            des = str(n-1) + str(col)
            g.addEdge(src, des)
    """ Adds edges right to left """
    for i in range(col, -1, -1):
        if pond_representation[row][i] == '*':
            if col == i+1:
                break
            src = str(row) + str(col)
            des = str(row) + str(i+1)
            g.addEdge(src, des)
            break
        elif i == 0:
            if col == 0:
                break
            src = str(row) + str(col)
            des = str(row) + str(0)
            g.addEdge(src, des)
    """ Adds edges bottom to top """
    for i in range(row, -1, -1):
        if pond_representation[i][col] == '*':
            if row == i+1:
                break
            src = str(row) + str(col)
            des = str(i+1) + str(col)
            g.addEdge(src, des)
            break
        elif i == 0:
            if row == 0:
                break
            src = str(row) + str(col)
            des = str(0) + str(col)
            g.addEdge(src, des)


def main():
    files = ['test0.txt', 'test1.txt', 'test3.txt', 'test2.txt']
    for file in files:
        print("----------" + file + "----------")
        g = Graph()
        with open(file) as f:
            firstline = f.readline()
            firstline = firstline.split()
            m = int(firstline[0])
            n = int(firstline[1])
            escape = int(firstline[2])
            exit = str(escape) + str(m-1)
            print("Exit is at node " + exit[::-1])
            pond_representation = [[0] * m] * n
            i = 0
            for line in f:
                print(line)
                line = line.split()
                pond_representation[i] = line
                i = i + 1
            """If the escape point if outside the pond"""
            if escape >= m or escape >= n:
                import sys
                print("There is NO escape from this Ice!! ")
                sys.exit()
            for i in range(m):
                for j in range(n):
                    create_graph(pond_representation, i, j, m, n, g)
            """ Ice maze is converted to a graph """
            max = 0
            for i in g.vertices:
                dijkpath = g.dijkstra(i, exit)
                if dijkpath:
                    if len(dijkpath) > max:
                        max = len(dijkpath)
            # max is the maximum length of the path
            count = 0
            while count <= max:
                node = []
                for i in g.vertices:
                    dijkpath = g.dijkstra(i, exit)
                    if dijkpath:
                        if count == len(dijkpath):
                            node.append(i[::-1])
                if count == 2:
                    node.append(exit[::-1])
                if count > 1:
                    print(str(count-1) + " : " + str(node))
                count = count + 1
            if count == 1:
                print("There is no way to GET OFF THE ICE !!")


if __name__ == '__main__':
    main()
