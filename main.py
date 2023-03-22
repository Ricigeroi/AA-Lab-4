import random
import time
import matplotlib.pyplot as plt
import networkx as nx


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
        graph = nx.Graph(self.adj_list)
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True)
        plt.show()

    def generate_random_graph(self, n, p):
        for i in range(n):
            self.add_vertex(i)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    self.add_edge(i, j)

    def bfs(self, start_vertex):
        output = []
        visited = {v: False for v in self.adj_list}
        queue = []

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            s = queue.pop(0)
            output.append(s)

            for neighbor in self.adj_list[s]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return output

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        output = []

        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                output.append(v)
                for neighbour in self.adj_list[v]:
                    stack.append(neighbour)

        return output


# Create a new graph object
g = Graph()

# Generate random graph
v = []
for i in range(1000, 10000, 1000):
    v.append(i)
e = 0.9

DFS_timing = []
BFS_timing = []

for i in v:
    g.generate_random_graph(i, e)
    x = random.randint(0, i)
    start_time = time.time()
    g.dfs(x)
    DFS_time = time.time() - start_time

    start_time = time.time()
    g.bfs(x)
    BFS_time = time.time() - start_time

    DFS_timing.append(DFS_time)
    BFS_timing.append(BFS_time)

print(v)
print(DFS_timing)
print(BFS_timing)


fig1 = plt.figure()
plt.grid()
plt.plot(v, DFS_timing, linewidth=2)
plt.plot(v, BFS_timing, linewidth=2)
plt.legend(['DFS', 'BFS'])
plt.title('Empirical analysis of DFS and BFS algorithms with edge density =' + str(e))
plt.xlabel('Number of vertices')
plt.ylabel('Execution time, sec')
plt.show()