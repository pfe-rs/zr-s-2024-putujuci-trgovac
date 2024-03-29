from Solver import Solver
from Graph import Graph
class User:
    def input_graph(self):
        n = int(input('Input the number of nodes:'))
        self.graph = Graph(n)
        m = int((n * (n - 1)) / 2)
        for i in range(m):
            u, v, w = map(int, input().split())
            self.graph.add_nodes_and_edge(u, v, w)
    def start_simulation(self):
        print(Solver.brute_force(self.graph.getEdges(), self.graph.getNumberOfNodes()))