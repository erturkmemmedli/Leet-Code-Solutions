# Alternative solution (which gives TLE error)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False
        target = [s // k] * k
        nums.sort(reverse = True)
        position = 0
        return self.dfs(nums, k, target, position)

    def dfs(self, nums, k, target, position):
        if position == len(nums):
            return True
        for i in range(k):
            if target[i] >= nums[position]:
                target[i] -= nums[position]
                if self.dfs(nums, k, target, position + 1):
                    return True
                target[i] += nums[position]
        return False
