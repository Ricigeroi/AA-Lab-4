import matplotlib.pyplot as plt
import networkx as nx
import time
import random
from queue import Queue

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def get_neighbors(self, vertex):
        return self.adj_list[vertex]

    def draw(self):
        G = nx.Graph(self.adj_list)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.show()

    def generate_random_graph(self, n, p):
        for i in range(n):
            self.add_vertex(i)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    self.add_edge(i, j)

    def bfs(self, start_vertex):
        visited = {v: False for v in self.adj_list}
        queue = []

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            s = queue.pop(0)
            print(s, end=' ')

            for neighbor in self.adj_list[s]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

def exec_time(function, n):
    start_time = time.time()
    function(n)
    end_time = time.time()
    return end_time - start_time

# create a new graph object
g = Graph()

g.generate_random_graph(5, 0.33)

# print the adjacency list
print(g.adj_list)


print(g.bfs(0))
print(g.bfs(1))
print(g.bfs(2))
print(g.bfs(3))
print(g.bfs(4))

g.draw()


