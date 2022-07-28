class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        avg = s / k
        if k >= len(nums): return avg
        for i in range(k, len(nums)):
            s = s + nums[i] - nums[i-k]
            avg = max(avg, s / k)
        return avg
