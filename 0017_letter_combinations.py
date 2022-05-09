class Solution:
    def __init__(self):
        self.hashmap = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}
        
    def letterCombinations(self, digits):
        if digits == "":
            return []
        num = ""
        output = []
        self.dfs(self.hashmap, output, digits, num)
        return output
    
    def dfs(self, hashmap, output, digits, num):
        if not digits:
            output.append(num)
            return
        for digit in self.hashmap[digits[0]]:
            self.dfs(self.hashmap, output, digits[1:], num + digit)
