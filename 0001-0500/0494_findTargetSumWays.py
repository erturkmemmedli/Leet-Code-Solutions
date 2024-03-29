class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        currentSum = 0
        index = 0
        self.memoization = {}
        zero_effect = 2 ** nums.count(0)
        nums = [i for i in nums if i]
        total = self.backtracing(nums, target, index, currentSum)
        return total * zero_effect

    def backtracing(self, nums, target, index, currentSum):
        if (index, currentSum) in self.memoization:
            return self.memoization[(index, currentSum)]
        if index == len(nums) and currentSum == target:
            return 1
        if index == len(nums):
            return 0
        positive = self.backtracing(nums, target, index + 1, currentSum + nums[index])
        negative = self.backtracing(nums, target, index + 1, currentSum - nums[index])
        self.memoization[(index, currentSum)] = positive + negative
        return self.memoization[(index, currentSum)]
    
# Alternative solution

from collections import defaultdict

class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hashmap = defaultdict(int, {0:1})
        for num in nums:
            level = defaultdict(int)
            for key in hashmap:
                level[key + num] += hashmap[key]
                level[key - num] += hashmap[key]
            hashmap = level
        return hashmap[target]

# Alternative solution (which gives TLE error)

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.output = 0
        self.visited = set()
        self.n = len(nums)
        zero_effect = 2 ** nums.count(0)
        self.dfs(nums, target, 0, [])
        return self.output * zero_effect

    def dfs(self, nums, target, path, pair):
        if not nums and len(pair) == self.n:
            pair = tuple(pair)
            if target == path and pair not in self.visited:
                self.visited.add(pair)
                self.output += 1
            return
        if not nums:
            return
        self.dfs(nums[1:], target, path + nums[0], pair + [nums[0]])
        self.dfs(nums[1:], target, path - nums[0], pair + [-nums[0]])

# Alternative solution

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        return self.dp(nums, target, 0)

    def dp(self, nums, target, index):
        if index == len(nums):
            return 1 if target == 0 else 0
        
        if (target, index) in self.memo:
            return self.memo[(target, index)]

        self.memo[(target, index)] = self.dp(nums, target - nums[index], index + 1) + self.dp(nums, target + nums[index], index + 1)
        return self.memo[(target, index)]
