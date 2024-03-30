from Solver import Solver
from Graph import Graph

class User:
    def input_graph(self):
        n = int(input('Input the number of nodes: '))
        self.graph = Graph(n)
        m = int((n * (n - 1)) / 2)
        for i in range(m):
            u, v, w = map(int, input().split())
            self.graph.add_nodes_and_edge(u, v, w)
        return self.graph
    
    def start_simulation(self, args):
        graph, type = args
        print("??")
        try:
            if type=="b": 
                f = True
                a, b = Solver.brute_force(self.graph.getEdges(), self.graph.getNumberOfNodes())
            elif type=="nn":
                f = True
                a, b = Solver.nearestNeighbor(graph)
            elif type == "sim":
                f = True
                a, b = Solver.simulated_annealing(self.graph.getEdges(), self.graph.getNumberOfNodes)
            if f:
                print(a, b)
                Solver.draw(a)
        except TypeError:
            print('Incorrect input, the methode you chose does not exist')
