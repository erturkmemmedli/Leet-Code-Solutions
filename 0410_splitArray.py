class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            total, count = 0, 1
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    count += 1
                    total = num
            if count > k:
                left = mid + 1
            else:
                right = mid
        return right
