class Solution:
    def calculate(self, s: str) -> int:
        return self.helper(s)[0]

    def helper(self, s):
        result = 0
        curr = ""
        plus = True
        i = 0
        index = None
        while i < len(s):
            if s[i] == '(':
                newResult, index = self.helper(s[i+1:])
                result += newResult if plus else -newResult
                i += index + 1
            elif s[i] == ')':
                if curr:
                    result += int(curr) if plus else -int(curr)
                i += 1
                return result, i
            elif s[i] == '+':
                if curr:
                    result += int(curr) if plus else -int(curr)
                    curr = ""
                plus = True
                i += 1
            elif s[i] == '-':
                if curr:
                    result += int(curr) if plus else -int(curr)
                    curr = ""
                plus = False
                i += 1
            elif s[i] == ' ':
                if curr:
                    result += int(curr) if plus else -int(curr)
                    curr = ""
                i += 1
                continue
            else:
                curr += s[i]
                i += 1
        if curr:
            result += int(curr) if plus else -int(curr)
        return result, i
        
# Alternative solution

class Solution:
    def calculate(self, s: str) -> int:
        return self.recursiveCalculation(s)[0]

    def helper(self, result, curr, plus, i):
        if curr:
            result += int(curr) if plus else -int(curr)
            curr = ""
        i += 1
        return result, curr, i

    def recursiveCalculation(self, s):
        result, curr, plus, index, i = 0, "", True, None, 0
        while i < len(s):
            if s[i] == '(':
                newResult, index = self.recursiveCalculation(s[i+1:])
                result += newResult if plus else -newResult
                i += index + 1
            elif s[i] == ')':
                result, curr, i = self.helper(result, curr, plus, i)
                return result, i
            elif s[i] == '+':
                [result, curr, i], plus = self.helper(result, curr, plus, i), True
            elif s[i] == '-':
                [result, curr, i], plus = self.helper(result, curr, plus, i), False
            elif s[i] == ' ':
                result, curr, i = self.helper(result, curr, plus, i)
            else:
                curr, i = curr + s[i], i + 1
        result, curr, _ = self.helper(result, curr, plus, i)
        return result, i
