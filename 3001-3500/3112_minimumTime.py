class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        answer = [inf] * n
        heap = [(0, 0)]

        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        while heap:
            time, node = heappop(heap)

            if answer[node] > time:
                answer[node] = time

                for child, cost in graph[node]:
                    if time + cost < disappear[child]:
                        heappush(heap, (time + cost, child))
                        
        return [i if i != inf else -1 for i in answer]
