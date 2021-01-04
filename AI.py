"""
    A python class that uses simple BFS to traverse a graph made of wiki links
"""

import collections #! Used rather than lists because of time complexity !#
from graph import *

class AI():
    def __init__(self, url=""):
        graph = Graph(url) #* Generate a graph *#
        self.bfs(graph, url)

    def dfs(self, graph, root):
        pass

    def bfs(self, graph, root):
        pass

    def a_star(self, graph, root):
        pass