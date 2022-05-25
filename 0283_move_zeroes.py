class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
