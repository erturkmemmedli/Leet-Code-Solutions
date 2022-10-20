class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # construction of graph
        graph = collections.defaultdict(list)
        for i, m in enumerate(manager):
            graph[m].append(i)
        # depth-first search
        self.timeNeeded = 0
        self.dfs(graph, headID, informTime, informTime[headID])
        return self.timeNeeded
        
    def dfs(self, graph, root, inform, minute):
        for child in graph[root]:
            self.dfs(graph, child, inform, minute + inform[child])
        self.timeNeeded = max(self.timeNeeded, minute)
        return
