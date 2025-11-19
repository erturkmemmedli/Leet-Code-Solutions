class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        enums = sorted([(i, num) for i, num in enumerate(nums)], key=lambda x: -x[1])[:k]
        return [num for i, num in sorted(enums, key = lambda x: x[0])]
