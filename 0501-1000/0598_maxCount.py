class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m, n

        for i, j in ops:
            if i < x:
                x = i
            if j < y:
                y = j

        return x * y
