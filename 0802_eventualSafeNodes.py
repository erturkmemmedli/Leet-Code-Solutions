class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.cyclicNodes = set()
        self.visited = [0] * len(graph)
        for i in range(len(graph)):
            if self.visited[i] == 0:
                self.foundCycle = 0
                self.cycleDetection(i, graph)
        return [i for i in range(len(graph)) if i not in self.cyclicNodes]            
        
    def cycleDetection(self, node, graph):
        print('bir',node, self.visited, self.foundCycle, self.cyclicNodes)
        if self.visited[node] == 1:
            self.foundCycle = 1
            self.cyclicNodes.add(node)
            return
        if self.visited[node] == 0:
            self.visited[node] = 1
            for neighbor in graph[node]:
                self.cycleDetection(neighbor, graph)
                if self.foundCycle == 1:
                    self.cyclicNodes.add(node)
                    return
            self.visited[node] = 2
