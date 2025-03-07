from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def __init__(self):
        self.memo = {}

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b, c in edges:
            graph[a - 1].append([b - 1, c])
            graph[b - 1].append([a - 1, c])

        distance = self.dijkstra(graph, n - 1, n)
        return self.dfs(graph, distance, 0, n)
    
    def dijkstra(self, graph, src, n):
        heap = [(0, src)]
        distance = [float('inf') for _ in range(n)]
        distance[src] = 0
        
        while heap:
            d, node = heappop(heap)

            for neighbor, cost in graph[node]:
                if distance[neighbor] > d + cost:
                    distance[neighbor] = d + cost
                    heappush(heap, (d + cost, neighbor))

        return distance

    def dfs(self, graph, distance, node, n):
        if node == n - 1:
            return 1

        if node in self.memo:
            return self.memo[node]
        
        result = 0

        for neighbor, _ in graph[node]:
            if distance[node] > distance[neighbor]:
                result = (result + self.dfs(graph, distance, neighbor, n)) % 1_000_000_007
        
        self.memo[node] = result
        return result
