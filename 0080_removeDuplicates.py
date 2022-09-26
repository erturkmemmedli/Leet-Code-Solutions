class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        base = 0
        count = 0
        while i < len(nums):
            if nums[i] == nums[base]:
                if  i - base - count == 1:
                    if i - base > 1:
                        nums[i], nums[i - count] = nums[i - count], nums[i]
                    i += 1
                else:
                    count += 1
                    i += 1
            else:
                base = i - count
                nums[i], nums[base] = nums[base], nums[i]
                i += 1
        return len(nums) - count
