class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # construction of graph
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        # find connected components by DFS
        self.connectedComponents = [0] * n
        self.visited = set()
        self.cc = 0
        for node in range(len(graph)):
            if node not in self.visited:
                self.dfs(graph, node)
                self.cc += 1
        # find how many additional cable we have
        totalUsable = {}
        for i, val in enumerate(self.connectedComponents):
            if val not in totalUsable:
                totalUsable[val] = [len(graph[i]), 1]
            else:
                totalUsable[val][0] += len(graph[i])
                totalUsable[val][1] += 1
        # compare bumber of additional cables and computers needing them
        cableNeeded = self.cc - 1
        additionalCables = 0
        for node, [cable, comp] in totalUsable.items():
            count = cable // 2
            additionalCables += count - comp + 1
        return cableNeeded if additionalCables >= cableNeeded else -1

    def dfs(self, graph, node):
        if node not in self.visited:
            self.visited.add(node)
            self.connectedComponents[node] = self.cc
            for child in graph[node]:
                if child not in self.visited:
                    self.dfs(graph, child)
