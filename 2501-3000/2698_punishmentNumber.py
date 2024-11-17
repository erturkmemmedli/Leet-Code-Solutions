class Solution:
    def punishmentNumber(self, n: int) -> int:
        num = 0
        
        for i in range(1, n+1):
            square = i * i
            if self.dfs(i, str(square), 0):
                num += square

        return num

    def dfs(self, n: int, s: str, curr: int) -> bool:
        if not s:
            return curr == n

        for i in range(len(s)):
            num = int(s[:i+1])
            if num + curr <= n:
                if self.dfs(n, s[i+1:], curr + num):
                    return True
