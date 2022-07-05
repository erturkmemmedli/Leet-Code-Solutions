class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        maximum = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            elif nums[j] == nums[i] + 1:
                maximum = max(maximum, j - i + 1)
                j += 1
            else:
                while i < j:
                    if nums[j] - nums[i] <= 1:
                        break
                    i += 1
                j += 1
        return maximum
