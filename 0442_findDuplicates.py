class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] != i+1:
                while nums[i] != nums[nums[i]-1]:
                    a, b = nums[i], nums[nums[i]-1]
                    nums[nums[i]-1], nums[i] = a, b
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result

# Alternative solution

class Solution:
    def findDuplicates(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        duplicates = []
        for i, num in enumerate(nums):
            if num != i + 1:
                duplicates.append(num)
        return duplicates
