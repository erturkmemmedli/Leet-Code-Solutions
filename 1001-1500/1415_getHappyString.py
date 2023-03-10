class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        output = []
        path = ""
        self.dfs(['a','b','c'], n, output, path)
        output.sort()
        return "" if k > len(output) else output[k-1]
        
    def dfs(self, letters, n, output, path):
        if len(path) == n:
            output.append(path)
            return
        for i in range(len(letters)):
            if not path:
                self.dfs(letters, n, output, path + letters[i])
            else:
                if path[-1] != letters[i]:
                    self.dfs(letters[i+1:] + letters[:i+1], n, output, path + letters[i])

# Alternative solution

class Solution1:
    def getHappyString(self, n: int, k: int) -> str:
        output = []
        path = ""
        self.dfs("abc", n, output, path)
        return "" if k > len(output) else output[k-1]
        
    def dfs(self, letters, n, output, path):
        if len(path) == n:
            output.append(path)
            return
        for letter in letters:
            if not path or path[-1] != letter:
                self.dfs(letters, n, output, path + letter)
