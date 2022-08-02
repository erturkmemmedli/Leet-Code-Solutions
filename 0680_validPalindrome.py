class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        part1 = s[i:j]
        part2 = s[i+1:j+1]
        return self.isPalindrome(part1) or self.isPalindrome(part2)
        
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

# Alternative solution

class Solution1:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        part1 = s[i:j]
        part2 = s[i+1:j+1]
        return part1 == part1[::-1] or part2 == part2[::-1]
