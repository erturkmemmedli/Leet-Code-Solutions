class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.visited = set()
        self.ranks = [float('inf')] * len(edges)

        return max(self.dfs(edges, i, 0) for i in range(len(edges)))

    def dfs(self, edges, node, rank):
        if node in self.visited or edges[node] == -1:
            return -1

        if self.ranks[node] < rank:
            return rank - self.ranks[node]

        self.ranks[node] = rank

        result = self.dfs(edges, edges[node], rank + 1)

        self.visited.add(node)
        
        return result
