class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        c = 0

        for i in range(len(nums)):
            if (s - nums[i]) / 2 == c:
                return i
            c += nums[i]
        
        return -1
