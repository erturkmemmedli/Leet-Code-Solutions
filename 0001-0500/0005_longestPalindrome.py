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

# Alternative solution

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        string = '-'.join('@{}!'.format(s))
        palindrom = [0] * len(string)
        center = 0
        right = 0
        for i in range(1, len(string) - 1):
            mirror = 2 * center - i
            if i < right:
                palindrom[i] = min(right - i, palindrom[mirror])
            while string[i - palindrom[i] - 1] == string[i + palindrom[i] + 1]:
                palindrom[i] += 1
            if palindrom[i] + i > right:
                center = i
                right = palindrom[i] + i
        length, index = max((p, i) for i, p in enumerate(palindrom))
        return string[index - length + 1: index + length : 2]

# Alternative solution

class Solution3:
    def longestPalindrome(self, s: str) -> str:
        self.palindrome = ""
        for i in range(len(s)):
            # odd palindrome
            self.find(s, i, i)
            # even paindrome
            self.find(s, i, i + 1)
        return self.palindrome

    def find(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(self.palindrome):
                self.palindrome = s[left : right + 1]
            left, right = left - 1, right + 1
