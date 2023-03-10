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

# Alternative solution

class Solution:
    def missingNumber(self, nums):
        nums.append(-1)
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i] != nums[j] and nums[i] != -1:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num == -1:
                return i
