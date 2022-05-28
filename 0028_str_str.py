class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

# Alternative solution

class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        hash_val = hash(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if hash_val == hash(haystack[i:i+len(needle)]):
                return i
        return -1
