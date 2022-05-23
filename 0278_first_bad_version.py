# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        old = 1
        new = n
        return self.binary_search(old, new)
    
    def binary_search(self, old, new):
        mid = (old + new) // 2
        if old == new:
            return new
        if not isBadVersion(mid):
            return self.binary_search(mid + 1, new)
        if isBadVersion(mid):
            return self.binary_search(old, mid)
