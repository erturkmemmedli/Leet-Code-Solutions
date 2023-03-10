class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] if i else [""] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

# Alternative solution

class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        path = ""
        self.dfs(n, output, path)
        return output
        
    def dfs(self, n, output, path):
        if len(path) == 2 * n:
            output.append(path)
            return
        for i in range(n):
            if path.count('(') < n:
                self.dfs(n, output, path + '(')
            if path.count('(') > path.count(')'):
                self.dfs(n, output, path + ')')
            return

# Alternative solution

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        result = []

        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    result.append("(" + left + ")" + right)

        return result
