class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.parent = [i for i in range(len(stones) + 1)]
        self.rank = [0 for _ in range(len(stones) + 1)]
        self.count = len(stones)
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union_by_rank_heuristic(i, j)
        return len(stones) - self.count
        
    def find_by_path_compression(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_by_path_compression(self.parent[x])
        return self.parent[x]
    
    def union_by_rank_heuristic(self, x, y):
        dx = self.find_by_path_compression(x)
        dy = self.find_by_path_compression(y)
        if dx == dy:
            return
        if self.rank[dx] < self.rank[dy]:
            self.parent[dx] = dy
            self.rank[dy] += self.rank[dx]
        else:
            self.rank[dx] += self.rank[dy]
            self.parent[dy] = dx
        self.count -= 1
            
# Alternative solution

class Solution1:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.parent = [i for i in range(len(stones))]
        self.union_by_rank_heuristic(stones)
        resultant = [self.find_by_path_compression(i) for i in range(len(stones))]
        return len(stones) - len(set(resultant))
        
    def find_by_path_compression(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_by_path_compression(self.parent[x])
        return self.parent[x]        
    
    def union_by_rank_heuristic(self, stones):
        X_map = {}
        Y_map = {}
        for i, coordinates in enumerate(stones):
            x, y = coordinates
            if x not in X_map:
                X_map[x] = i
            if y not in Y_map:
                Y_map[y] = i
            self.parent[self.find_by_path_compression(Y_map[y])] = self.parent[self.find_by_path_compression(X_map[x])]
            self.parent[self.find_by_path_compression(X_map[x])] = self.find_by_path_compression(i)
            
# Alternative solution

from collections import defaultdict

class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        for x, y in stones:
            rows[x].append(y)
            cols[y].append(x)
        coordinates = {(i, j) for i, j in stones}
        count = 0
        for i, j in stones:
            if (i, j) in coordinates:
                self.dfs(rows, cols, coordinates, i, j)
                count += 1
        return len(stones) - count
        
    def dfs(self, rows, cols, coordinates, x, y):
        coordinates.discard((x, y))
        for i in rows[x]:
            if (x, i) in coordinates:
                self.dfs(rows, cols, coordinates, x, i)
        for j in cols[y]:
            if (j, y) in coordinates:
                self.dfs(rows, cols, coordinates, j, y)
