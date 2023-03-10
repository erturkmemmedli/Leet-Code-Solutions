class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        visited = set()
        mask = (1 << n) - 1
        heap = [(0, i, 1 << i) for i in range(n)]
        while heap:
            distance, node, state = heapq.heappop(heap)
            if state == mask:
                return distance
            for kid in graph[node]:
                if (state | 1 << kid, kid) not in visited:
                    visited.add((state | 1 << kid, kid))
                    heapq.heappush(heap, (distance + 1, kid, state | 1 << kid))
