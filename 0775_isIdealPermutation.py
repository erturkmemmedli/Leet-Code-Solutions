class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(i - num) <= 1 for i, num in enumerate(nums))
        
# Alternative solution

class Solution1:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if not (i - 1 <= nums[i] <= i + 1):
                return False
        return True

# Alternative solution

class Solution2:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        first, second = nums[0], None
        for i in range(1, len(nums)):
            if second == None and nums[i] > nums[i-1]:
                first = nums[i]
            elif second == None and nums[i] == nums[i-1] - 1:
                second = nums[i]
            elif nums[i] < nums[i-1] - 1:
                return False
            elif second != None and nums[i] > first:
                first, second = nums[i], None
            elif second != None and nums[i] < second:
                return False
        return True
