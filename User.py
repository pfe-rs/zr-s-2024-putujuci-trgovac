from Solver import Solver
from Graph import Graph
class User:
    def input_graph(self):
        n = int(input('Unesi broj cvorova:'))
        self.graph = Graph(n)
        m = int((n * (n - 1)) / 2)
        for i in range(m):
            u, v, w = map(int, input().split())
            self.graph.add_nodes_and_edge(u, v, w)
        return self.graph
    def start_simulation(self,graph:Graph):
        print("Izaberi nacin resavanja (b->brute force   nn-> nearest neighbor   sim -> simulated annealing)")
        type=input()
        try:
            if type=="b": 
                f = True
                a, b = Solver.brute_force(self.graph.getEdges(), self.graph.getNumberOfNodes())
            elif type=="nn":
                f = True
                a, b = Solver.nearestNeighbor(graph)
            elif type == "sim":
                f = True
                a, b = Solver.simulated_annealing(self.graph.getEdges(), list(range(1, self.graph.getNumberOfNodes())))
            if f:
                print(a, b)
                Solver.draw(a)
        except TypeError:
            print('Pogresan unos, nacin resavanja koji ste izabrali ne postoji.')
        print("Unesi broj gradova u podruti:")
        n = int(input())
        perm = []
        for i in range(n):
            x = int(input())
            perm.append(x)
        try:
            a, b = Solver.simulated_annealing(self.graph.getEdges(), perm)
            print(a, b)
            Solver.draw(a)
        except TypeError:
            print('Pogresan unos, ova podruta je nemoguca.')
