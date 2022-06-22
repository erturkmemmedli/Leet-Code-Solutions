from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        odd = False
        for v in count.values():
            if v % 2 == 0:
                result += v
            else:
                result += v - 1
                odd = True
        return result + 1 if odd else result
