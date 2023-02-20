class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacecy_matrix = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjacecy_matrix[b].append(a)
        visited = [0] * numCourses
        self.cycyleFound = 0
        for i in range(numCourses):
            if self.cycyleFound == 1:
                break
            if visited[i] == 0:
                self.cycle_detection(adjacecy_matrix, visited, i)
        return self.cycyleFound == 0
        
    def cycle_detection(self, adjacecy_matrix, visited, node):
        if visited[node] == 1:
            self.cycyleFound = 1
            return
        if visited[node] == 2:
            return
        visited[node] = 1
        for neighbor in adjacecy_matrix[node]:
            self.cycle_detection(adjacecy_matrix, visited, neighbor)
        visited[node] = 2
        
# Alternative solution

class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacecy_matrix = [[] for _ in range(numCourses)]
        visit_counts = [0] * numCourses
        for a, b in prerequisites:
            adjacecy_matrix[b].append(a)
            visit_counts[a] += 1
        queue = deque([i for i in range(numCourses) if visit_counts[i] == 0])
        visited = set()
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in adjacecy_matrix[node]:
                    visit_counts[neighbor] -= 1
                    if visit_counts[neighbor] == -1:
                        return False
                    if visit_counts[neighbor] == 0:
                        queue.append(neighbor)
        return len(visited) == numCourses

# Alternative solution

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        in_degree = {i : 0 for i in range(numCourses)}
        
        for start, end in prerequisites:
            graph[end].append(start)
            in_degree[start] += 1
            
        queue = deque()
        
        for node, degree in in_degree.items():
            if degree == 0:
                queue.append(node)
        
        output = []
        
        while queue:
            node = queue.popleft()
            output.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return len(output) == numCourses
