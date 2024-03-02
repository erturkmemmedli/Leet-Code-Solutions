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

# Alternative solution

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for a, b in redEdges:
            graph[a].append((b, 'red'))
        
        for a, b in blueEdges:
            graph[a].append((b, 'blue'))

        answer = [None] * n

        def dijkstra(source, destination):
            heap = [(0, source, None)]
            visited = set()

            while heap:
                distance, node, state = heappop(heap)
                visited.add((node, state))

                if node == destination:
                    return distance

                for neighbor, color in graph[node]:
                    if color != state and (neighbor, color) not in visited:
                        heappush(heap, (distance + 1, neighbor, color))

            return -1

        for i in range(n):
            answer[i] = dijkstra(0, i)

        return answer

# Alternative solution

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # contruct graph with n nodes
            # key in graph -> neighbors (blue, red)
            # bfs or dfs
            # in each step, we must be in different color

        graph = {i : [] for i in range(n)}

        for node1, node2 in redEdges:
            graph[node1].append((node2, 'red'))
        
        for node1, node2 in blueEdges:
            graph[node1].append((node2, 'blue'))

        # shortest path from 0 to each node
            # dijkstra (heap)

        shortest_paths = [-1] * n
        heap = [(0, 0, None)]
        distance = [[float('inf'), float('inf')] for _ in range(n)]
        distance[0] = [0, 0]

        while heap:
            dist, node, curr_color = heappop(heap)
            shortest_paths[node] = min(distance[node])
            
            for neighbor, color in graph[node]:
                if color != curr_color and distance[neighbor][0 if color == 'red' else 1] > dist + 1:
                    distance[neighbor][0 if color=='red' else 1] = dist + 1
                    heappush(heap, (dist + 1, neighbor, color))

        return shortest_paths
