class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = {}
        visited = set()
        distance = [[inf, inf] for _ in range(len(edges))]

        for i, node in enumerate(edges):
            if node != -1:
                graph[i] = node

        def dfs(node, curr, idx):
            if node in visited:
                return
            distance[node][idx] = curr
            if node not in graph:
                return
            visited.add(node)
            dfs(graph[node], curr + 1, idx)

        dfs(node1, 0, 0)
        visited = set()
        dfs(node2, 0, 1)

        res, idx = inf, None
        for i, [a, b] in enumerate(distance):
            if max(a, b) < res:
                res = max(a, b)
                idx = i
        
        return idx if res != inf else -1
