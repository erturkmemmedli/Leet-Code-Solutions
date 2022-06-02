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
            self.DFS(nums[:i] + nums[i+1:], result, temp + [nums[i]])

# Alternative solution

class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, result, [])
        return result
    
    def backtrack(self, nums, result, temp):
        if len(nums) == 0:
            result.append(temp.copy())
            return
        else:
            for i, n in enumerate(nums):
                temp.append(n)
                self.backtrack(nums[i+1:] + nums[:i], result, temp)
                temp.pop()
                
# Alternative solution

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, result, [])
        return result
    
    def backtrack(self, nums, result, temp):
        if len(nums) == 0:
            result.append(temp)
            return
        else:
            for i, n in enumerate(nums):
                self.backtrack(nums[i+1:] + nums[:i], result, temp + [n])
