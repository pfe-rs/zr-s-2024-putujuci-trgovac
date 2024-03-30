import Graph
import Solver
from multiprocessing import Pool, cpu_count
def indexSort(listPrice):
    for i  in range (len(listPrice)):
        for j in range (len(listPrice)):
            if listPrice[i][0]<listPrice[j][0]:
                pom=listPrice[i][0]
                listPrice[i][0]=listPrice[j][0]
                listPrice[j][0]=pom

#def findRange(graph,prices,roads):
#   for i in range(len(roads)):
#      listPrice=[prices,roads]
#      indexSort(listPrice)
#      pivot=len(roads)//2
#      min=9999
#      while....:
            
