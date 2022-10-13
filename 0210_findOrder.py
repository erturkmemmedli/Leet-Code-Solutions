class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct the graph
        self.graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            self.graph[b].append(a)
        # cycle detection
        self.cycleFound = 0
        self.visited = [0] * numCourses
        self.postorder = [[i, 0] for i in range(numCourses)]
        self.clock = 0
        for i in range(numCourses):
            if self.cycleFound == 1:
                return []
            if self.visited[i] == 0:
                self.cycleDetection(i)
        # unless cycle is detected, topological sort
        return self.topologicalSort()

    def cycleDetection(self, node):
        if self.cycleFound == 1:
            return
        if self.visited[node] == 1:
            self.cycleFound = 1
        if self.visited[node] == 0:
            self.visited[node] = 1
            for neighbor in self.graph[node]:
                self.cycleDetection(neighbor)
            self.visited[node] = 2
            self.postorder[node][1] = self.clock
            self.clock += 1            

    def topologicalSort(self):
        order = sorted(self.postorder, key = lambda x: x[1], reverse = True)
        order = [index for index, node in order]
        return order
