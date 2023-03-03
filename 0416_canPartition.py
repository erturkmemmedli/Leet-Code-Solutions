class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        subset_total = total // 2
        mxm = max(nums)
        if mxm > subset_total: return False
        elif mxm == subset_total: return True
        hashset = {subset_total}
        for num in nums:
            if num in hashset:
                return True
            for item in hashset.copy():
                hashset.add(item - num)
        return False

# Alternative solution

class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        half = total // 2
        mxm = max(nums)
        if mxm > half: return False
        elif mxm == half: return True
        dp = [False] * (half + 1)
        dp[0] = True
        for num in nums:
            for i in range(half, num-1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[half]

# Alternative solution

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        self.memo = {}
        return self.dp(nums, s//2, 0)

    def dp(self, nums, target, index):
        if target == 0:
            return True

        if target < 0 or index == len(nums):
            return False

        if (target, index) in self.memo:
            return self.memo[(target, index)]

        self.memo[(target, index)] = self.dp(nums, target - nums[index], index + 1) or self.dp(nums, target, index + 1)
        return self.memo[(target, index)]
