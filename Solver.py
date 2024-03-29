import numpy as np
from Graph import Graph

#from Shapes import Circle
#from Shapes import Line
#from User import User
class Solver:
    def __init__(self,type):
        pass

        
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
    
    def nearestNeighbor(graph:Graph):
        visited=[1]
        price=0
        possible_edges=np.array(graph.edges[1])
        next=1
        while (len(visited)!= graph.nodes):
            possible_edges[0]=999
            possible_edges[next]=999
            potential_next=np.argmin(possible_edges)
            if(potential_next in visited):
                 possible_edges[potential_next]=999
            
            else:
                next=potential_next
                price=price+min(possible_edges)
                possible_edges=np.array(graph.edges[next])
                visited.append(next)
        price+=graph.edges[next][1]
        print("Put " + str(visited) + " je posecen sa cenom " + str(price))
        return(visited,price)


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