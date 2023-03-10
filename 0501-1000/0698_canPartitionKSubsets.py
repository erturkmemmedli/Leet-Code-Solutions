class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False
        nums.sort(reverse = True)
        subsetSum = s // k
        subset = [subsetSum] * k
        position = 0
        return self.dfs(nums, k, subsetSum, subset, position)

    def dfs(self, nums, k, subsetSum, subset, position):
        if position == len(nums):
            return True
        for i in range(k):
            if subset[i] >= nums[position]:
                subset[i] -= nums[position]
                if self.dfs(nums, k, subsetSum, subset, position + 1):
                    return True
                subset[i] += nums[position]
                if subset[i] == subsetSum:
                    break
        return False
