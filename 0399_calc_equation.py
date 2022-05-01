from collections import deque

class Solution:
    def calcEquation(self, equations, values, queries):
        adj = {}
        for i in range(len(equations)):
            if equations[i][0] not in adj:
                adj[equations[i][0]] = [] 
            if equations[i][1] not in adj:
                adj[equations[i][1]] = []
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1 / values[i]))
        output = []
        for q in queries:
            if q[0] not in adj or q[1] not in adj:
                output.append(-1)
                continue
            Q = deque([])
            Q.append((q[0], 1))
            visited = set()
            while Q:
                vertex, product = Q.popleft()
                if vertex == q[1]:
                    output.append(product)
                    break
                visited.add(vertex)
                for neighbor, value in adj[vertex]:
                    if neighbor not in visited:
                        Q.append((neighbor, product * value))
                if not Q:
                    output.append(-1)
        return output
    
# Alternative solution
    
class Solution1:
    def DFS(self, adj, visited, start, end, mult):
        if start == end:
            return mult
        visited.add(start)
        if start in adj:
            for neighbor, value in adj[start]:
                if neighbor not in visited:
                    result = self.DFS(adj, visited, neighbor, end, mult * value)
                    if result != -1:
                        return result
        return -1
    
    def calcEquation(self, equations, values, queries):
        adj = {}
        for i in range(len(equations)):
            if equations[i][0] not in adj:
                adj[equations[i][0]] = [] 
            if equations[i][1] not in adj:
                adj[equations[i][1]] = []
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1 / values[i]))
        output = []
        for q in queries:
            if q[0] not in adj or q[1] not in adj:
                output.append(-1)
                continue
            if q[0] == q[1]:
                output.append(1)
                continue
            else:
                visited = set()
                output.append(self.DFS(adj, visited, q[0], q[1], 1))
        return output
