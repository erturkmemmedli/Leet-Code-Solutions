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

# Alternative solution

class Solution1:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.backtrack(s, len(s), result, '')
        return result
    
    def backtrack(self, s, n, result, temp):
        if s == '':
            result.append(temp)
            return
        else:
            if not s[0].isalpha():
                self.backtrack(s[1:], n, result, temp + s[0])
            else:
                self.backtrack(s[1:], n, result, temp + s[0].lower())
                self.backtrack(s[1:], n, result, temp + s[0].upper())

# Alternative solution

class Solution2:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = []
        path = ""
        self.dfs(s, output, path, len(s))
        return output
    
    def dfs(self, string, output, path, n):
        if len(path) == n:
            output.append(path)
            return
        if 48 <= ord(string[0]) <= 57:
            self.dfs(string[1:], output, path + string[0], n)
        else:
            self.dfs(string[1:], output, path + string[0].lower(), n)
            self.dfs(string[1:], output, path + string[0].upper(), n)

# Alternative solution

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        combinations = deque([""])

        for char in s:
            for _ in range(len(combinations)):
                string = combinations.popleft()

                if char.isdigit():
                    new_string = string + char

                    if len(new_string) == len(s):
                        result.append(new_string)
                    else:
                        combinations.append(new_string)

                else:
                    new_string1 = string + char.lower()
                    new_string2 = string + char.upper()

                    if len(new_string1) == len(s):
                        result.append(new_string1)
                        result.append(new_string2)
                    else:
                        combinations.append(new_string1)
                        combinations.append(new_string2)

        return result
