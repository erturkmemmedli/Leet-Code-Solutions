class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if self.binarySearch(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def binarySearch(self, bloomDay, m, k, day):
        bouquet, flower = 0, 0
        for bloom in bloomDay:
            if bloom > day:
                flower = 0
            else:
                bouquet += (flower + 1) // k
                flower = (flower + 1) % k
        return bouquet >= m
