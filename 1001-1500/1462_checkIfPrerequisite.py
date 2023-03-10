class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        degree = [0 for _ in range(numCourses)]
        hierarchy = [set() for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
            degree[b] += 1
            hierarchy[b].add(a)
        queue = collections.deque(i for i, deg in enumerate(degree) if deg == 0)
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                hierarchy[child] |= hierarchy[node]
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)
        return [a in hierarchy[b] for a, b in queries]
        
class Solution1:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        floydWarshall = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            floydWarshall[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    floydWarshall[i][j] = floydWarshall[i][j] or (floydWarshall[i][k] and floydWarshall[k][j])
        return [floydWarshall[a][b] for a, b in queries]

# Alternative solution (which gives TLE error)

class Solution2:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            self.graph[a].append(b)
        queryResults = []
        for a, b in queries:
            self.visited = set()
            queryResults.append(True if self.dfs(a, b) else False)
        return queryResults

    def dfs(self, start, end):
        if start == end:
            return True
        if start not in self.visited:
            self.visited.add(start)
        for child in self.graph[start]:
            if self.dfs(child, end):
                return True
                
# Alternative solution (which gives TLE error)

class Solution3:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            self.graph[a].append(b)
        self.hierarchy = [set() for _ in range(numCourses)]
        for i in range(numCourses):
            self.topologicalSort(i, i)
        queryResults = []
        for a, b in queries:
            queryResults.append(True if a in self.hierarchy[b] else False)
        return queryResults

    def topologicalSort(self, node, parent):
        for child in self.graph[node]:
            self.topologicalSort(child, parent)
            if parent != node:
                self.hierarchy[child].add(parent)
        if parent != node:
            self.hierarchy[node].add(parent)
