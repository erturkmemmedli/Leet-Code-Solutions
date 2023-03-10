class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left = nums[0]
        seperation = None
        index = None
        for i in range(1, len(nums)):
            if nums[i] < left and seperation is None:
                continue
            elif nums[i] >= left and seperation is None:
                seperation = nums[i]
                index = i
            elif nums[i] >= seperation:
                seperation = nums[i]
            elif left <= nums[i] < seperation:
                continue
            elif nums[i] < left:
                left = seperation
                seperation = None
        return index
