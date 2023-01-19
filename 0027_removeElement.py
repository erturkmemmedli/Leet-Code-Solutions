class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[i] != val and nums[j] != val:
                i += 1
                j += 1
            elif nums[j] == val:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return i
                
# Alternative solution

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        j = len(nums) - 1
        count = 0
        while j >= 0:
            if nums[j] == val:
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
                j -= 1
                i -= 1
            else:
                j -= 1
        return len(nums) - count   

# Alternative solution

class Solution:
    def removeElement(self, nums, val):
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i
