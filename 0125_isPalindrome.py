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
