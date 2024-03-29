class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1

# Alternative solution

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = -1
        for i in range(len(nums)):
            if not nums[i]:
                if zero < 0:
                    zero = i
                else:
                    continue
            else:
                if zero < 0:
                    continue
                else:
                    nums[i], nums[zero] = nums[zero], nums[i]
                    zero += 1
        return nums

# Alternative solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
