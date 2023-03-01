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

# Alternative solution

class Solution1:
    def __init__(self):
        self.hashmap = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return
        output = []
        self.dfs(digits, output, "", 0)
        return output
        
    def dfs(self, digits, output, path, i):
        if len(digits) == len(path):
            output.append(path)
            return
        for char in self.hashmap[digits[i]]:
            self.dfs(digits, output, path + char, i + 1)

# Alternative solution

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        self.hashmap = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}

        self.result = []
        self.backtrack(digits, "")
        return self.result

    def backtrack(self, digits, path):
        if not digits:
            self.result.append(path)
            return
        for letter in self.hashmap[digits[0]]:
            self.backtrack(digits[1:], path + letter)
