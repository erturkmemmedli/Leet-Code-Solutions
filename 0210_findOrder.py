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
        
# Alternative solution

class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct the graph inversely
        self.graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            self.graph[a].append(b)
        # cycle detection and topological sort
        self.cycleFound = 0
        self.visited = [0] * numCourses
        self.postorder = []
        for i in range(numCourses):
            if self.cycleFound == 1:
                return []
            if self.visited[i] == 0:
                self.cycleDetection(i)
        return self.postorder

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
            self.postorder.append(node)
        return order

# Alternative solution

from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        
        for course, preq_course in prerequisites:
            graph[preq_course].append(course)
            in_degree[course] += 1
            
        queue = deque()
        
        for course, preq_count in in_degree.items():
            if preq_count == 0:
                queue.append(course)
                
        topologically_sorted_courses = []
        
        while queue:
            node = queue.popleft()
            topologically_sorted_courses.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return topologically_sorted_courses if len(topologically_sorted_courses) == numCourses else []
