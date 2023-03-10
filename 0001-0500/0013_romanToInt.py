class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if s[i] == 'M':
                if i == 0 or (i > 0 and s[i-1] != 'C'):
                    result += 1000
                else:
                    result += 800
            if s[i] == 'D':
                if i == 0 or (i > 0 and s[i-1] != 'C'):
                    result += 500
                else:
                    result += 300
            if s[i] == 'C':
                if i == 0 or (i > 0 and s[i-1] != 'X'):
                    result += 100
                else:
                    result += 80
            if s[i] == 'L':
                if i == 0 or (i > 0 and s[i-1] != 'X'):
                    result += 50
                else:
                    result += 30
            if s[i] == 'X':
                if i == 0 or (i > 0 and s[i-1] != 'I'):
                    result += 10
                else:
                    result += 8
            if s[i] == 'V':
                if i == 0 or (i > 0 and s[i-1] != 'I'):
                    result += 5
                else:
                    result += 3
            if s[i] == 'I':
                result += 1
        return result
    
# Alternative solution

class Solution1:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        integer = d[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if d[s[i]] < d[s[i+1]]:
                integer -= d[s[i]]
            else:
                integer += d[s[i]]
        return integer
