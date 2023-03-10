from math import log2

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        step = int(1 + log2(n))
        self.binary_lift = [[-1] * step for _ in range(n)]
        for j in range(step):
            for i in range(n):
                if j == 0:
                    self.binary_lift[i][j] = parent[i]
                elif self.binary_lift[i][j-1] != -1:
                    self.binary_lift[i][j] = self.binary_lift[self.binary_lift[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            step = int(log2(k))
            node = self.binary_lift[node][step]
            k -= (1 << step)
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

# Alternative solution (which gives Time Limit Exceeded (TLE) error)

class TreeAncestor1:
    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.parent = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k):
            if node == -1:
                return -1
            node = self.parent[node]
        return node
        
# Alternative solution (which gives Memory Limit Exceeded (MLE) error)

class TreeAncestor2:
    def __init__(self, n: int, parent: List[int]):
        self.hashmap = {}
        for i in range(1, n):
            temp = i
            while temp:
                if i not in self.hashmap:
                    self.hashmap[i] = [(1, parent[temp])]
                else:
                    self.hashmap[i].append((self.hashmap[i][-1][0] + 1, parent[temp]))
                temp = parent[temp]
            
    def getKthAncestor(self, node: int, k: int) -> int:
        if node == 0 or len(self.hashmap[node]) < k:
            return -1
        else:
            return self.hashmap[node][k-1][1]
