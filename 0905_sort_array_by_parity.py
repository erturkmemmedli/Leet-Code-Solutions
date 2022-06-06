class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                pivot += 1
                continue
        return nums
    
# Alternative solution

class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pointer = 0
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                i += 1
                pointer += 1
            elif nums[i] % 2 == 1:
                i += 1
        return nums
