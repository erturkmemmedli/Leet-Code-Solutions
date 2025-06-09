class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mods = {0: 0, 1: 0}
        ends = {0: 0, 1: 0}
        for i in range(len(nums)):
            mods[nums[i] % 2] += 1
            ends[nums[i] % 2] = ends[1 - nums[i] % 2] + 1
        return max(max(mods.values()), max(ends.values()))
