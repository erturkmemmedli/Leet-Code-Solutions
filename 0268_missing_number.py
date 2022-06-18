class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = n * (n+1) // 2
        for i in nums:
            target -= i
        return target

# Alternative solution

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = n * (n+1) // 2
        return target - sum(nums)
