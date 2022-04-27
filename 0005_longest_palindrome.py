class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        matrix = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if s[i] == s[j]:
                    matrix[i][j] = 1
        for k in range(len(matrix)-1):
            if k == 0:
                if matrix[k][k+1] == 0:
                    continue
                else:
                    result = s[0:2]
                    continue            
            if matrix[k-1][k+1] == 1:
                step = 0
                to_bottom = k - 1
                to_right = k + 1
                while to_bottom >= 0 and to_right < len(matrix) and matrix[to_bottom][to_right] == 1:
                    step += 1
                    result = max(result, s[k-step:k+step+1], key = len)
                    to_bottom -= 1
                    to_right += 1
            if matrix[k][k+1] == 1:
                step = 0
                to_bottom = k - 1
                to_right = k + 2
                result = max(result, s[k:k+2], key = len)
                while to_bottom >= 0 and to_right < len(matrix) and matrix[to_bottom][to_right] == 1:
                    step += 1
                    result = max(result, s[k-step:k+step+2], key = len)
                    to_bottom -= 1
                    to_right += 1         
        return result
		
# Alternative solution

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        pointer = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                result = max(result, s[pointer : i+1], key = len)
            else:
                pointer = i
            j = 1
            while i - j >= 0 and i + j < len(s):
                if i == pointer:
                    if s[i-j] == s[i+j]:
                        result = max(result, s[i-j : i+j+1], key = len)
                        j += 1
                    else:
                        break
                else:
                    if s[pointer-j] == s[i+j]:
                        result = max(result, s[pointer-j : i+j+1], key = len)
                        j += 1
                    else:
                        break
        return result
