from collections import defaultdict, deque

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = defaultdict(set)
        indegree = defaultdict(int)
        pool = {i: 1 for i in range(n)}
        fuel = 0

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
            indegree[a] += 1
            indegree[b] += 1

        queue = deque([i for i in range(n) if i != 0 and indegree[i] == 1])

        while queue:
            node = queue.popleft()
            fuel += math.ceil(pool[node] / seats)

            for child in graph[node]:
                pool[child] += pool[node]
                graph[child].remove(node)
                indegree[child] -= 1

                if indegree[child] == 1 and child != 0:
                    queue.append(child)

        return fuel
