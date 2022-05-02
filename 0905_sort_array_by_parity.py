class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                pivot += 1
                continue
        return nums