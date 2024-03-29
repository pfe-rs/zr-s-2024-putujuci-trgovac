import numpy
class Solver:
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