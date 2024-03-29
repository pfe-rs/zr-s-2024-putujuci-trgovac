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
        self.graph.print_graph()
        return self.graph
    def start_simulation(self,graph:Graph):
        print("Izaberi nacin resavanja(b->brute force   nn-> nearest neighbor   sim -> simulated annealing)")
        solver=Solver(input())
        try:
            if solver.type=="brute":            
                print(solver.brute_force(self.graph.getEdges(), self.graph.getNumberOfNodes()))
            elif solver.type=="nn":
                Solver.nearestNeighbor(graph)
        except TypeError:
            print('Incorrect input, the methode you chose does not exist')