class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        result = []
        temp = []
        self.recursion(nums, k, result, temp)
        return result
        
    def recursion(self, nums, k, result, temp):
        if len(temp) == k:
            result.append(temp)
            return
        for i in range(len(nums)):
            self.recursion(nums[i+1:], k, result, temp + [nums[i]])
