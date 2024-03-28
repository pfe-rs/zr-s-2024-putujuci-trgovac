import numpy

def next_permutation(perm):
    n = len(perm)
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1
    perm[i], perm[j] = perm[j], perm[i]
    perm[i + 1:] = reversed(perm[i + 1:])
    return True


class Solver:
    def brute_force(edges, n):
        perm = list(range(1, n))
        sol = 1e18
        bestperm = []
        while True:
            current = 0
            for i in range(n - 1):
                current += edges[perm[i]][perm[i - 1]]
            if current < sol:
                sol = current
                bestperm = perm[:]
            next_permutation(perm)
            if  perm[0] != 1:
                break
        return (bestperm, sol)

class Client:
    def input_graph(self):
        n = int(input('Input the number of nodes:'))
        self.graph = Graph(n)
        m = int((n * (n - 1)) / 2)
        for i in range(m):
            u, v, w = map(int, input().split())
            self.graph.add_nodes_and_edge(u, v, w)
        self.graph.print_graph()
    def start_simulation(self):
        print(Solver.brute_force(self.graph.getEdges(), self.graph.getNumberOfNodes()))

class Graph:
    def __init__(self, n):
        self.nodes = n
        self.edges = numpy.zeros((n + 5, n + 5))

    def add_nodes_and_edge(self, u, v, w):
        try:
            if w <= 0:
                print('Edge weight error.')
                return
            self.edges[u][v] = w
            self.edges[v][u] = w
        except TypeError:
            print('Incorrect weight type.')

    def print_graph(self):
        print('GRAPH:')
        print(self.edges)
    def getNumberOfNodes(self):
        return self.nodes + 1
    def getEdges(self):
        return self.edges

client = Client()
client.input_graph()
client.start_simulation()