class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.graph = collections.defaultdict(list)
        for i, num in enumerate(arr):
            if i - num >= 0:
                self.graph[i].append(i - num)
            if i + num < len(arr):
                self.graph[i].append(i + num)
        if arr[start] == 0:
            return True
        self.visited = set()
        return self.dfs(start)

    def dfs(self, start):
        if start in self.visited:
            return False
        if start not in self.graph:
            return False 
        self.visited.add(start)
        for node in self.graph[start]:
            if start == node:
                return True
            if self.dfs(node):
                return True
        self.visited.remove(start)
