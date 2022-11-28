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
