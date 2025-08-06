from collections import defaultdict
from heapq import heappop, heappush
from math import inf

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        distance = [inf] * self.n
        distance[node1] = 0
        heap = [(0, node1)]
        while heap:
            dist, node = heappop(heap)
            if node == node2:
                return dist
            for child, cost in self.graph[node]:
                if distance[child] > dist + cost:
                    distance[child] = dist + cost
                    heappush(heap, (dist + cost, child))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
