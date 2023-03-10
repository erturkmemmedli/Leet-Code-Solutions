class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        DP = [0] * (target + 1)
        for num in nums:
            if num <= target:
                DP[num] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                DP[i] += DP[i - num]
        return DP[-1]
