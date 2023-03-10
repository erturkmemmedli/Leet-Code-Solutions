class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def bfs(i):
            heap = [(0, i)]
            distance = [float("inf") if i != j else 0 for j in range(n)]
            while heap:
                weight, node = heapq.heappop(heap)
                for child, cost in graph[node]:
                    if distance[child] > weight + cost:
                        distance[child] = weight + cost
                        if distance[child] <= distanceThreshold:
                            heapq.heappush(heap, (distance[child], child))
                            cities[i][1].add(child)
        graph = collections.defaultdict(list)
        for start, end, weight in edges:
            graph[start].append((end, weight))
            graph[end].append((start, weight))
        cities = [(i, set()) for i in range(n)]
        for i in range(n):
            bfs(i)
        cities.sort(key = lambda x: [len(x[1]), -x[0]])
        return cities[0][0]
