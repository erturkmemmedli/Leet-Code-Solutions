class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prefix = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 0:
                prefix.append(nums[i] - nums[i-1])
        if not prefix: return 1
        wiggle = 0
        for i in range(1, len(prefix)):
            if prefix[i] * prefix[i-1] < 0:
                wiggle += 1
        return wiggle + 2
