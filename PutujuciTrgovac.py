import numpy as np
from Solver import Solver
from Graph import Graph
from User import User
import multiprocessing

if __name__ == "__main__":
    user = User()
    graph=user.input_graph()
    #user.start_simulation(graph,type)
    #road=(input(print("izaberi rutu")))
    #print(road)
    #minGraph= graph.minimizeGraph(road)
    k=int(input("Unesi broj podruti: "))
    print("unesi zeljeno vreme")
    

    tests = []
    type=[]
    for i in range(k):
        j=0
        road=[]
        q=int(input('Unesi duzinu rute: '))
        while j!=q:
            x=int(input())
            road.append(x)
            j=j+1
        minGraph = graph.minimizeGraph(road)
        minGraph.print_graph()
        way_of_solving = input('Izaberi nacin resavanja (b->brute force   nn-> nearest neighbor   sim -> simulated annealing) ')
        type=(way_of_solving)
        i=i+1
        tests.append((minGraph, type))

    print('[Multiprocessing] Start...')
    n = len(tests)
    with multiprocessing.Pool(processes = n) as pool:
        pool.map(user.start_simulation, tests)

    graph.minimizeGraph(road)

'''
1 2 10
1 3 15
1 4 20
2 3 35
2 4 25
3 4 30
'''