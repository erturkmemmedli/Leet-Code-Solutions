from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start, end in paths:
            graph[start].append(end)
            graph[end].append(start)
        flowers = [0] * n
        for i in range(n):
            temp = []
            for garden in graph[i+1]:
                temp.append(flowers[garden-1])
            for j in range(1, 5):
                if j not in temp:
                    flowers[i] = j
                    break
        return flowers

# Alternative solution

class Solution1:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in paths:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        flowers = [0] * n
        mapping = {i : {1, 2, 3, 4} for i in range(n)}
        for i in range(n):
            if flowers[i] == 0:
                queue = collections.deque([(i, mapping[i])])
                while queue:
                    node, choice = queue.popleft()
                    if flowers[node]:
                        continue
                    select = choice.pop()
                    flowers[node] = select
                    for neighbor in graph[node]:
                        if flowers[neighbor] == 0:
                            mapping[neighbor] &= ({1, 2, 3, 4} - {select})
                            queue.append((neighbor, mapping[neighbor]))
        return flowers
