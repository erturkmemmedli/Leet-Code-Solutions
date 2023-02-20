class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: return list(range(n))
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = [key for key, val in graph.items() if len(val) == 1]
        seen = {i for i in leaves}
        queue = collections.deque([leaves])
        while len(graph) > 2:
            level = queue.popleft()
            newLevel = []
            for leaf in level:
                candidate = graph[leaf].pop()
                del graph[leaf]
                graph[candidate].remove(leaf)
                if len(graph[candidate]) == 1 and candidate not in seen:
                    seen.add(candidate)
                    newLevel.append(candidate)
            if newLevel:
                queue.append(newLevel)
        return queue[0]

# Alternative solution

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        graph = {i: [] for i in range(n)}
        in_degree = {i: 0 for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            in_degree[a] += 1
            in_degree[b] += 1
        
        queue = deque([key for key, val in in_degree.items() if val == 1])

        MHT = []

        while queue:
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                in_degree[node] -= 1

                for neighbor in graph[node]:
                    if in_degree[neighbor] == 0:
                        continue

                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 1:
                        queue.append(neighbor)

            if queue:
                MHT = list(queue)
            
        return MHT
