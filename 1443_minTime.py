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
