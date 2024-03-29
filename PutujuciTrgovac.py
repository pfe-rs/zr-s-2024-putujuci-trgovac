import numpy
from Solver import Solver
from Graph import Graph
from User import User



user = User()
graph=user.input_graph()
user.start_simulation(graph)