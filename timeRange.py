import Graph
import Solver
import mpmath as math
from multiprocessing import Pool, cpu_count
def findRange(prices,roads,time):
    unordered = []
    for i in range(len(roads)):
        unordered.append(prices[i], roads[i])
    ordered = sorted(unordered, key = lambda x : x[0])
    ret = 0
    L = 0
    R = len(roads) - 1
    while L <= R:
        S = (L + R) // 2
        if ordered[S][0] < time:
            L = S + 1
        else:
            ret = S
            R = S - 1
    if abs(time - ordered[ret - 1][0]) < abs(time - ordered[ret][0]): return ordered[ret - 1]
    else: return ordered[ret]