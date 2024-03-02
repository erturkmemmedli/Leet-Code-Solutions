from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [None for _ in range(len(graph))]
        for i in range(len(graph)):
            if color[i] is None:
                color[i] = 'W'
                Q = deque([i])
                while len(Q) != 0:
                    vertex = Q.popleft()
                    for path in graph[vertex]:
                        if color[path] is None:
                            if color[vertex] == 'W':
                                Q.append(path)
                                color[path] = 'B'
                            if color[vertex] == 'B':
                                Q.append(path)
                                color[path] = 'W'
                        else:
                            if (color[vertex] == 'W' and color[path] == 'W') or (color[vertex] == 'B' and color[path] == 'B'):
                                return False
        return True

# Alternative solution

class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.visited = set()
        self.color = [0] * len(graph) # all nodes are colorless at start
        for i in range(len(graph)):
            if i not in self.visited:
                self.color[i] = 1 # color initializes as 1 - Red
                if not self.bfs(graph, i):
                    return False
        return True
            
    def bfs(self, graph, i):
        queue = collections.deque([i])
        while queue:
            node = queue.popleft()
            if node not in self.visited:
                self.visited.add(node)
                for neighbor in graph[node]:
                    if self.color[node] == self.color[neighbor]: # same neighboring colors means not bipartite
                        return False
                    if neighbor not in self.visited:
                        if self.color[node] == 1: # if node is 1 - Red, neigbor is 2 - Black
                            self.color[neighbor] = 2
                        if self.color[node] == 2:
                            self.color[neighbor] = 1 # if node is 2 - Black, neigbor is 1 - Red
                        queue.append(neighbor)
        return True

# Alternative solution

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [None] * n

        for i in range(len(graph)):
            if color[i] == None:
                color[i] = 0
                queue = deque([i])

                while queue:
                    node = queue.popleft()

                    for neighbor in graph[node]:
                        if color[neighbor] == color[node]:
                            return False
                        if color[neighbor] == None:
                            color[neighbor] = color[node] ^ 1
                            queue.append(neighbor)
                
        return True
