from  Solver import Solver
from User import User
from Graph import Graph

import pytest
import random
import numpy

#@pytest.fixture
def test_add():
    n = int(random.randint(4, 4))
    graph=Graph(n)
    edges = numpy.zeros((n + 1, n + 1))
    for i in range(1, n + 1):
        for j in range(1, i):
            if i - j == 1 or i - j == n - 1:
                edges[i][j] = 1
                edges[j][i] = 1
                graph.add_nodes_and_edge(i,j,1)
            else:
                graph.add_nodes_and_edge(i,j,random.randint(10,100))
                edges[i][j] = random.randint(10, 100)
                edges[j][i] = edges[i][j]
    print(edges)
    #assert Solver.brute_force(edges, n + 1) == (list(range(1, n + 1)), n)
    assert Solver.nearestNeighbor(graph) == (list(range(1, n + 1 )), n)