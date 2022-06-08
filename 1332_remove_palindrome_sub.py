class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 0 if not s else 1 if s == s[::-1] else 2
