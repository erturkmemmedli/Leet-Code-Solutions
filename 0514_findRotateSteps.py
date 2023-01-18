class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.graph = collections.defaultdict(list)
        for i, char in enumerate(ring):
            self.graph[char].append(i)
        self.memo = {}
        return self.dfs(key, len(ring), 0)

    def dfs(self, key, length, currIndex):
        if not key:
            return 0
        if (key, currIndex) in self.memo:
            return self.memo[(key, currIndex)]
        result = float("inf")
        for i in self.graph[key[0]]:
            distance = min(abs(currIndex - i), length - abs(currIndex - i))
            result = min(result, distance + 1 + self.dfs(key[1:], length, i))
        self.memo[(key, currIndex)] = result
        return result
