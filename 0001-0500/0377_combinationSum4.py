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

# Alternative solution

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.combination_count = 0
        self.memo = {}
        return self.backtrack(nums, target)
    
    def backtrack(self, nums, target):
        if target in self.memo:
            return self.memo[target]

        if target == 0:
            return 1

        self.memo[target] = 0

        for i in range(len(nums)):
            if target - nums[i] >= 0:
                self.memo[target] += self.backtrack(nums, target - nums[i])

        return self.memo[target]
