class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        edges = collections.deque(edges)
        self.reverseGraph = {}
        while edges:
            a, b = edges.popleft()
            if a == 0:
                self.reverseGraph[b] = a
            else:
                if b in self.reverseGraph:
                    self.reverseGraph[a] = b
                elif a in self.reverseGraph:
                    self.reverseGraph[b] = a
                else:
                    edges.append([a, b])
        appleNodes = [i for i, has in enumerate(hasApple) if has]
        self.visited = set()
        for node in appleNodes:
            self.traverseTree(node)
        return len(self.visited) * 2

    def traverseTree(self, node):
        if node not in self.visited and node in self.reverseGraph:
            self.visited.add(node)
            self.traverseTree(self.reverseGraph[node])        

# Alternative solution

class Solution1:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.graph = collections.defaultdict(list)
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.visited = set()
        return max(self.traverseTree(0, hasApple) - 2, 0)

    def traverseTree(self, node, hasApple):
        if node in self.visited:
            return 0
        self.visited.add(node)
        second = 0
        for child in self.graph[node]:
            second += self.traverseTree(child, hasApple)
        if second > 0:
            return second + 2
        return 2 if hasApple[node] else 0
