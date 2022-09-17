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

# Alternative solution

from collections import defaultdict

class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashmap = defaultdict(list)
        for i, [a, b] in enumerate(equations):
            hashmap[a].append((b, values[i]))
            hashmap[b].append((a, 1/values[i]))
        output = []
        for x, y in queries:
            if x not in hashmap or y not in hashmap:
                output.append(-1)
            elif x == y:
                output.append(1)
            else:   
                res = self.dfs(hashmap, x, y, set())
                if res == 0:
                    output.append(-1)
                else:
                    output.append(res)
        return output
            
    def dfs(self, hashmap, start, end, visited):
        if start == end:
            return 1
        if start not in visited:
            visited.add(start)
            for path, val in hashmap[start]:
                res = self.dfs(hashmap, path, end, visited)
                if res:
                    return val * res
        return 0

# Alternative solution

from collections import defaultdict

class Solution3:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashmap = defaultdict(list)
        for i, [a, b] in enumerate(equations):
            hashmap[a].append((b, values[i]))
            hashmap[b].append((a, 1/values[i]))
        output = []
        for x, y in queries:
            if x not in hashmap or y not in hashmap:
                output.append(-1)
            elif x == y:
                output.append(1)
            else:   
                output.append(self.dfs(hashmap, x, y, set(), 1))
        return output
            
    def dfs(self, hashmap, start, end, visited, result):
        if start == end:
            return result
        if start not in visited:
            visited.add(start)
            for path, val in hashmap[start]:
                ans = self.dfs(hashmap, path, end, visited, val * result)
                if ans != -1:
                    return ans
        return -1
