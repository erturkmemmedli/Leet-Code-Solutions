class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count

# Alternative solution

class Solution1:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n = n >> 1
        return count
