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

# Alternative solution

class Solution1:
    def firstBadVersion(self, n: int) -> int:
        return self.binary_search(1, n)
        
    def binary_search(self, l, r):
        m = (l + r) // 2
        if isBadVersion(m):
            if m == l or r == l+1:
                return m
            return self.binary_search(l, m)
        else:
            if m == r or l == r-1:
                return r
            return self.binary_search(m, r)
