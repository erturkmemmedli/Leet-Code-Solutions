class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = [i for i in range(len(s))]
        # union by rank heuristic
        self.rank = [0 for _ in range((len(s)))]
        # find and union pairs
        for a, b in pairs:
            self.union(a, b)
        # last step to get final connection between points
        for i in range(len(s)):
            self.find(i)
        charMap = collections.defaultdict(list)
        for i, p in enumerate(self.parent):
            charMap[p].append(s[i])
        for key, val in charMap.items():
            charMap[key] = sorted(val, reverse = True)
        answer = []
        for p in self.parent:
            answer.append(charMap[p].pop())
        return "".join(answer)

    def find(self, i):
        if self.parent[i] != i:
            # path compression
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        dx = self.find(x)
        dy = self.find(y)
        if dx == dy:
            return
        if self.rank[dx] > self.rank[dy]:
            self.parent[dy] = dx
        elif self.rank[dx] < self.rank[dy]:
            self.parent[dx] = dy
        else:
            self.parent[dx] = dy
            self.rank[dy] += 1
