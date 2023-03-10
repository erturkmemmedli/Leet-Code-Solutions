class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        L = [nums[0]]
        for i in range(1, len(nums)):
            L.append(nums[i] + L[-1])
        m = min(L)
        return -1 * m + 1 if m < 0 else 1
