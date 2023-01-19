class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for char in s:
            if 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
                new += char
        for i in range(len(new)//2):
            if new[i] != new[len(new) - 1 - i]:
                return False
        return True

# Alternative solution

class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while not (s[left].isalpha() or s[left].isdigit()) and left < right:
                left += 1
            while not (s[right].isalpha() or s[right].isdigit()) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
