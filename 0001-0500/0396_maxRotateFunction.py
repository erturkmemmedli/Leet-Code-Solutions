class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = sum([i * num for i, num in enumerate(nums)])
        s = sum(nums)
        k = len(nums)
        result = f
        while nums:
            f += s - k * nums.pop()
            result = max(result, f)
        return result
