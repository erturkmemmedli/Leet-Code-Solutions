class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        n = len(s)
        self.dfs(s, n, result, '')
        return result
    
    def dfs(self, s, n, result, temp):
        if n == len(temp):
            result.append(temp)
            return
        for i in range(len(s)):
            if s[i] in '0123456789':
                self.dfs(s[i+1:], n, result, temp + s[i])
            else:
                self.dfs(s[i+1:], n, result, temp + s[i].upper())
                self.dfs(s[i+1:], n, result, temp + s[i].lower())
