class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        result = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
                result = max(result, zeros + ones)
            if s[i] == '1':
                ones -= 1
                result = max(result, zeros + ones)
        return result
