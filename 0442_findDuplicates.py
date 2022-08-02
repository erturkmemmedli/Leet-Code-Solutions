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
