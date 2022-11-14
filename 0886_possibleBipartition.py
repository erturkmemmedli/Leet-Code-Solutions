class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        colors = [0] * n
        for i in range(n):
            if not colors[i]:
                queue = collections.deque([i])
                colors[i] = 1
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if colors[neighbor] == 0:
                            if colors[node] == 1:
                                colors[neighbor] = 2
                            if colors[node] == 2:
                                colors[neighbor] = 1
                            queue.append(neighbor)
                        elif (colors[neighbor] == 1 and colors[node] == 1) or (colors[neighbor] == 2 and colors[node] == 2):
                            return False
        return True
