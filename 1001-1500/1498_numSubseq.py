class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        left = 0
        right = bisect.bisect_left(nums, target - nums[0] + 1) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                total = (total + 2 ** (right - left)) % 1_000_000_007
                left += 1
            else:
                right -= 1
        return total 
