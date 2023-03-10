class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.parent = {char: char for char in string.ascii_lowercase}
        for first, equality, _, second in equations:
            if equality == "=":
                self.parent[self.find(first)] = self.find(second)
        return not any(equality == "!" and self.find(first) == self.find(second) for first, equality, _, second in equations)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
# Alternative solution

class Solution1:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.graph = {char : set() for char in string.ascii_lowercase}
        for start, condition, _, end in equations:
            if condition == "=":
                self.graph[start].add(end)
                self.graph[end].add(start)
        for start, condition, _, end in equations:
            if condition == "!":
                self.visited = set()
                self.flag = False
                if self.dfs(start, end):
                    return False
        return True

    def dfs(self, start, end):
        if start == end:
            self.flag = True
            return True
        if start not in self.visited:
            self.visited.add(start)
            for element in self.graph[start]:
                if element not in self.visited:
                    self.dfs(element, end)
                    if self.flag:
                        return True
