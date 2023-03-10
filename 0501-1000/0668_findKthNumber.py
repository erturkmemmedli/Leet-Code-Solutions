class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            isEnough = self.enough(m, n, k, mid)
            if isEnough:
                high = mid
            else:
                low = mid + 1
        return low

    def enough(self, row, col, k, val):
        count = 0
        for i in range(1, row + 1):
            count += min(col, val // i)
        return count >= k
