class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        self.DFS(nums, result, temp)
        return result
    
    def DFS(self, nums, result, temp):
        if not nums:
            result.append(temp)
            return
        for i in range(len(nums)):
            self.DFS(nums[i+1:] + nums[:i], result, temp + [nums[i]])
