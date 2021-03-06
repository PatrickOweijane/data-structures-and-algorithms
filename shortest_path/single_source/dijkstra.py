from heapq import heappush, heappop
from math import inf

def dijkstra(adjacency_matrix, source):
    '''
    assumes that all weights are positive
    adjacency_matrix represents a weighted graph
    '''
    number_of_vertices = len(adjacency_matrix)
    shortest_d = [inf] * number_of_vertices
    predecessor = [None] * number_of_vertices
    seen = [False] * number_of_vertices
    heap = [(0, source, None)]
    while heap:
        d, v, pred = heappop(heap)
        if seen[v]: continue
        seen[v] = True
        shortest_d[v] = d
        predecessor[v] = pred
        for u, weight in enumerate(adjacency_matrix[v]):
            if weight == inf or seen[u]: continue
            heappush(heap, (d + weight, u, v))
    return shortest_d, predecessor
