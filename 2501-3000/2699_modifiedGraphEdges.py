class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = [{} for i in range(n)]
        distance = [float('inf')] * n

        for a, b, w in edges:
            graph[a][b] = w
            graph[b][a] = w

        def dijkstra(heap, edges, distance):
            while heap:
                dist, node = heappop(heap)

                for neighbor, d in graph[node].items():
                    if d != -1 and dist + d < distance[neighbor]:
                        heappush(heap, (dist + d, neighbor))
                        distance[neighbor] = dist + d
                    
        def fill(edges):
            for i, [a, b, w] in enumerate(edges):
                if w == -1:
                    edges[i][2] = 2 * 10 ** 9

            return edges

        heap = ([(0, source)])
        distance[source] = 0
        dijkstra(heap, edges, distance)

        if distance[destination] == target:
            return fill(edges)

        if distance[destination] < target:
            return []

        for i, [a, b, w] in enumerate(edges):
            if w == -1:
                edges[i][2] = 1
                graph[a][b] = edges[i][2]
                graph[b][a] = edges[i][2]

                heap = [(distance[a], a), (distance[b], b)]
                dijkstra(heap, edges, distance)

                if distance[destination] == target:
                    return fill(edges)

                if distance[destination] < target:
                    edges[i][2] += target - distance[destination]
                    graph[a][b] = edges[i][2]
                    graph[b][a] = edges[i][2]
                    return fill(edges)
        
        return []
