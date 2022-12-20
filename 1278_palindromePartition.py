class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        self.memo = {}
        return self.dfs(s, k)
    
    def dfs(self, string, k):
        if (string, k) in self.memo:
            return self.memo[(string, k)]
        if len(string) == k:
            return 0
        if k == 1:
            result = sum([string[i] != string[-1 - i] for i in range(len(string) // 2)])
        else:
            result = float('inf')
            for i in range(1, len(string) - k + 2):
                result = min(result, self.dfs(string[:i], 1) + self.dfs(string[i:], k - 1))
        self.memo[(string, k)] = result
        return result
