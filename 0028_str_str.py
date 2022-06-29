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

# Alternative solution

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        string = needle + '-' + haystack
        lps = self.KMP_prefix(string)
        for i in range(len(needle)+1, len(string)):
            if lps[i] == len(needle):
                return i - 2 * len(needle)
        return -1
        
    def KMP_prefix(self, pattern):
        prefix = [0] * len(pattern)
        border = 0
        for i in range(1, len(pattern)):
            while border > 0 and pattern[i] != pattern[border]:
                border = prefix[border - 1]
            if pattern[i] == pattern[border]:
                border += 1
            else:
                border = 0
            prefix[i] = border
        return prefix
