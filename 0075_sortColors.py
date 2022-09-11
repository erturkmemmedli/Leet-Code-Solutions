class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for num in nums:
            if num == 0:
                zero += 1
            if num == 1:
                one += 1
            if num == 2:
                two += 1
        i = 0
        while i < len(nums):
            if zero:
                nums[i] = 0
                zero -= 1
            elif one:
                nums[i] = 1
                one -= 1
            elif two:
                nums[i] = 2
            i += 1
            
# Alternative solution

class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        nums[:] = [0] * nums.count(0) + [1] * nums.count(1) + [2] * nums.count(2)

# Alternative solution
        
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        for i, num in enumerate(nums):
            if num == 2:
                continue
            if num == 1:
                nums[i], nums[one] = nums[one], nums[i]
                one += 1
            if num == 0:
                nums[i], nums[one] = nums[one], nums[i]
                nums[one], nums[zero] = nums[zero], nums[one]
                zero += 1
                one += 1
