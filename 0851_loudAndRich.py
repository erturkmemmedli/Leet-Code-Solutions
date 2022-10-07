class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        self.graph = [[] for _ in range(n)]
        for a, b in richer:
            self.graph[b].append(a)
        self.answer = [None] * n
        for i in range(len(self.graph)):
            self.dfs(i, quiet)
        return self.answer

    def dfs(self, node, quiet):
        if self.answer[node] is None:
            self.answer[node] = node
            for neighbor in self.graph[node]:
                candidate = self.dfs(neighbor, quiet)
                if quiet[candidate] < quiet[self.answer[node]]:
                    self.answer[node] = candidate
        return self.answer[node]
