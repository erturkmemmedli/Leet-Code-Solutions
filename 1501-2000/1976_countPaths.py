class Solution:
    def countPaths(self, n, roads):
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        heap = [(0, 0)]
        distance = [float('inf')] * n
        count = [0] * n

        distance[0] = 0
        count[0] = 1

        while heap:
            dist, node = heappop(heap)

            if node == n-1:
                return count[node] % 1_000_000_007

            for neighbor, cost in graph[node]:
                candidate = dist + cost

                if candidate == distance[neighbor]:
                    count[neighbor] += count[node]

                elif candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))
                    count[neighbor] = count[node]
