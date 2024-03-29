from collections import deque

class Solution:
    def networkDelayTime(self, times, n, k):
        distance = [float('inf')] * n
        visited = [False] * n
        adj = [[] for _ in range(n)]
        cost = [[] for _ in range(n)]
        for i in range(len(times)):
            adj[times[i][0] - 1].append(times[i][1] - 1)
            cost[times[i][0] - 1].append(times[i][2])
        Q = deque([k - 1])
        distance[k - 1] = 0
        while Q:
            vertex = Q.popleft()
            if not visited[vertex]:
                visited[vertex] = True
                for neighbor in adj[vertex]:
                    if distance[neighbor] == float('inf'):
                        Q.append(neighbor)
                    weight = adj[vertex].index(neighbor)
                    if distance[neighbor] > distance[vertex] + cost[vertex][weight]:
                        distance[neighbor] = distance [vertex] + cost[vertex][weight]
                        Q.append(neighbor)
                        visited[neighbor] = False
        return -1 if max(distance) == float('inf') else max(distance)

# Alternative solution

from collections import deque

class Solution1:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n)]
        cost = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u - 1].append(v - 1)
            cost[u - 1].append(w)
        print(graph, cost)
        distance = [inf] * n
        distance[k - 1] = 0
        queue = deque([k - 1])
        while queue:
            node = queue.popleft()
            for i, neighbor in enumerate(graph[node]):
                if distance[neighbor] > distance[node] + cost[node][i]:
                    distance[neighbor] = distance[node] + cost[node][i]
                    queue.append(neighbor)
        delayTime = max(distance)
        return delayTime if delayTime != inf else -1
