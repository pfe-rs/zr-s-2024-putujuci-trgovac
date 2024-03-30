import numpy
class Graph:
    def __init__(self, n):
        self.nodes = n
        self.edges = numpy.zeros((n + 1, n + 1))

    def add_nodes_and_edge(self, u, v, w):
        try:
            if w <= 0:
                print('Greska tezine veze.')
                return
            self.edges[u][v] = w
            self.edges[v][u] = w
        except TypeError:
            print('Pogresan tip tezine veze.')

    def print_graph(self):
        print('GRAF:')
        print(self.edges)
    def getNumberOfNodes(self):
        return self.nodes + 1
    def getEdges(self):
        return self.edges