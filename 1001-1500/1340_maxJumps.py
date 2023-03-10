class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        self.memo = collections.defaultdict(int)
        maxVisit = 0
        for i in range(len(arr)):
            maxVisit = max(maxVisit, self.dfs(arr, i, d))
        return maxVisit
        
    def dfs(self, arr, idx, d):
        if idx in self.memo: return self.memo[idx]
        length = 0
        for i in range(idx + 1, idx + d + 1):
            if len(arr) <= i or arr[i] >= arr[idx]: break
            length = max(length, self.dfs(arr, i, d))
        for i in range(idx - 1, idx - d - 1, -1):
            if i < 0 or arr[i] >= arr[idx]: break
            length = max(length, self.dfs(arr, i, d))
        self.memo[idx] = length + 1
        return self.memo[idx]
