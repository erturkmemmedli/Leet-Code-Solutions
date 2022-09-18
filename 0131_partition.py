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
