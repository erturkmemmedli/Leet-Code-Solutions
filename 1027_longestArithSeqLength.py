class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp_map = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dp_map[(j, nums[j] - nums[i])] = dp_map.get((i, nums[j] - nums[i]), 1) + 1
        return max(dp_map.values())
