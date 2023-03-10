class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        prefix = [1] * len(nums)

        for i in range(len(nums)):
            prefix[(i + 1 - nums[i]) % len(nums)] -= 1

        for i in range(1, len(nums)):
            prefix[i] += prefix[i-1]

        return prefix.index(max(prefix))
