import numpy
import mpmath as math
from multiprocessing import Pool, cpu_count
class Graph:
    def __init__(self, n):
        self.nodes = n
        self.edges = numpy.zeros((n + 1, n + 1))

    def add_nodes_and_edge(self, u, v, w):
        try:
            if w <= 0:
                print('Edge weight error.')
                return
            self.edges[u][v] = w
            self.edges[v][u] = w
        except TypeError:
            print('Incorrect weight type.')
    def joinGraph(self,matrix):
        for i in range(self.nodes+1):
            for j in range(self.nodes+1):
                self.edges[i][j]=matrix[i][j]

        
    def print_graph(self):
        print('GRAPH:')
        print(self.edges)
    def getNumberOfNodes(self):
        return self.nodes + 1
    def getEdges(self):
        return self.edges
    def minimizeGraph(self,indexes):
        graph=Graph(self.nodes)
        graph.joinGraph(self.edges)
        currNumberOfNodes = len(indexes)
        i=1
        while(currNumberOfNodes!=self.nodes):
            if(i not in indexes):
                for j in range(self.nodes+1):
                    graph.edges[i][j]=math.inf
                    graph.edges[j][i]=math.inf
                    #self.edges[i][j]=math.inf
                    #self.edges[j][i]=math.inf
                currNumberOfNodes = currNumberOfNodes+1
            i=i+1
            #self.print_graph()
        return graph
        