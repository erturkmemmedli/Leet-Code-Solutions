class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = collections.defaultdict(list)
        for fr, to in tickets:
            self.graph[fr].append(to)
        for node, neighbors in self.graph.items():
            self.graph[node] = sorted(neighbors, reverse = True)
        self.EulerPath = []
        self.dfs("JFK")
        return self.EulerPath[::-1]

    def dfs(self, node):
        while self.graph[node]:
            kid = self.graph[node].pop()
            self.dfs(kid)
        self.EulerPath.append(node)
