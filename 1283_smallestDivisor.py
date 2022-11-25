class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, max(nums) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if sum([math.ceil(num / mid) for num in nums]) <= threshold:
                right = mid
            else:
                left = mid
        return right
