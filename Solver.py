import numpy
import mpmath as math
import networkx as nx
import matplotlib.pyplot as plt
import random



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

def randomize_permutation(perm):
    method = random.randint(1, 3)
    if method == 1:
        a = random.randint(0, len(perm) - 1)
        b = b = random.randint(0, len(perm) - 1)
        while b == a: b = random.randint(0, len(perm) - 1)
        if a > b: a, b = b, a
        rev = perm[a:b + 1]
        perm[a:b + 1] = rev[::-1]
    elif method == 2:
        a = random.choice(perm)
        perm.remove(a)
        b = random.choice(perm)
        perm.insert(perm.index(b), a)
    elif method == 3:
        a = random.choice(range(len(perm)))
        b = random.choice(range(len(perm)))
        perm[a], perm[b] = perm[b], perm[a]
    else:
        next_permutation(perm)
    return perm

class Solver:
    def draw(perm):
        graph = []
        picked = []
        for i in range(len(perm)):
            for j in range(i):
                graph.append((j + 1, i + 1))
        for i in range(len(perm)):
            picked.append((min(perm[i], perm[i - 1]), max(perm[i], perm[i - 1])))
        G = nx.Graph()
        G.add_edges_from(graph)
        colors = {}
        for edge in G.edges():
            if edge in picked: colors[edge] = 'skyblue'
            else: colors[edge] = 'black'
        nx.draw(G, with_labels = True, node_color = 'skyblue', edge_color = [colors[edge] for edge in G.edges()], node_size = 800, font_size = 12)
        plt.gcf().canvas.manager.set_window_title('TSP:')
        plt.show()
    def get_permutation_score(edges, perm):
        ret = 0
        for i in range(len(perm)):
            ret += edges[perm[i]][perm[i - 1]]
        return ret
    def brute_force(edges, n):
        perm = list(range(1, n))
        sol = 1e18
        bestperm = []
        while True:
            current = Solver.get_permutation_score(edges, perm)
            if current < sol:
                sol = current
                bestperm = perm[:]
            next_permutation(perm)
            if  perm[0] != 1:
                break
        return (bestperm, sol)
    def simulated_annealing(edges, n):
        temperature = 500
        perm = list(range(1, n))
        modded_perm = perm[:]
        sol = Solver.get_permutation_score(edges, perm)
        bestperm = perm
        iterations = 1000000 / n
        while iterations > 0:
            modded_perm = randomize_permutation(perm)
            perm_score = Solver.get_permutation_score(edges, perm)
            modded_score = Solver.get_permutation_score(edges, modded_perm)
            delta = perm_score - modded_score
            if delta > 0:
                perm = modded_perm[:]
                if perm_score < sol:
                    sol = perm_score
                    bestperm = perm[:]
            else:
                if random.uniform(0, 1) <= math.exp(float(delta) / float(temperature)):
                    perm = modded_perm[:]
            temperature *= 0.99
            iterations -= 1
        return bestperm, int(sol)