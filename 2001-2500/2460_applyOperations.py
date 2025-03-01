class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        i = j = 0
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] != 0:
                i += 1
            j += 1
                  
        return nums
