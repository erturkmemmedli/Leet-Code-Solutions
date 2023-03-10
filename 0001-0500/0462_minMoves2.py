class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n % 2 == 1:
            median = nums[n//2]
        else:
            median = (nums[n//2 - 1] + nums[n//2]) // 2
        output = 0
        for num in nums:
            output += abs(num - median)
        return output
