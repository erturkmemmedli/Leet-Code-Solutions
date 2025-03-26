class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for row in grid:
            nums.extend(row)

        nums.sort()

        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) % x != 0:
                return -1

        mid = len(nums) // 2
        target = nums[mid]
        result = 0

        for num in nums:
            result += abs(num - target) // x

        return result
