class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        self.permutations = set()
        self.memoization = set()
        self.findPermutations(nums, [])
        return len(self.permutations)

    def findPermutations(self, nums, path):
        if (tuple(nums), tuple(path)) in self.memoization:
            return
        if not nums:
            self.permutations.add(tuple(path))
            return
        for i in range(len(nums)):
            if not path or self.isSquare(nums[i], path[-1]):
                self.findPermutations(nums[:i] + nums[i+1:], path + [nums[i]])
            self.memoization.add((tuple(nums), tuple(path)))

    def isSquare(self, num1, num2):
        x = num1 + num2
        return int(x ** 0.5) == x ** 0.5
