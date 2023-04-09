class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for start, end in edges:
            graph[start].append(end)
            indegree[end] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 0])
        count = [[0] * 26 for _ in range(n)]

        while queue:
            node = queue.popleft()
            count[node][ord(colors[node]) - ord('a')] += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                count[neighbor] = [max(a, b) for a, b in zip(count[node], count[neighbor])]

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max(max(i) for i in count) if sum(indegree) == 0 else -1
