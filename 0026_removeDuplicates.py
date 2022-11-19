class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] > nums[i]:
                if j == i + 1:
                    i += 1
                    j += 1
                else:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
            else:
                j += 1
        return len(set(nums))

# Alternative solution

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[j], nums[i+1] = nums[i+1], nums[j]
                i += 1
                j += 1
        return i+1
