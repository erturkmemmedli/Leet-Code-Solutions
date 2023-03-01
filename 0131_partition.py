class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        path = []
        self.dfs(s, output, path)
        return output 
    
    def dfs(self, string, output, path):
        if not string:
            output.append(path)
            return
        for i in range(len(string)):
            sub = string[:i+1]
            if self.isPalindrom(sub):
                self.dfs(string[i+1:], output, path + [sub])
                
    def isPalindrom(self, string):
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

# Alternative solution

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.backtrack(s, [])
        return self.result

    def backtrack(self, string, path):
        if not string:
            self.result.append(path)
            return
        for i in range(len(string)):
            substring = string[:i+1]
            if substring == substring[::-1]:
                self.backtrack(string[i+1:], path + [substring])
