class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in redEdges:
            graph[a].append((b, 'red'))
        for u, v in blueEdges:
            graph[u].append((v, 'blue'))
        distance = [[float('inf'), float('inf')] for _ in range(n)] # index 0 is red, index 1 is blue
        heap = [(0, 0, None)]
        while heap:
            cost, node, edge = heapq.heappop(heap)
            for child, color in graph[node]:
                if color == 'red' and edge != 'red':
                    if distance[child][0] > cost + 1:
                        distance[child][0] = cost + 1
                        heapq.heappush(heap, (distance[child][0], child, color))       
                if color == 'blue' and edge != 'blue':
                    if distance[child][1] > cost + 1:
                        distance[child][1] = cost + 1
                        heapq.heappush(heap, (distance[child][1], child, color))
        distance[0] = 0
        for i in range(1, n):
            minimum = min(distance[i])
            distance[i] = minimum if minimum != float('inf') else -1
        return distance
