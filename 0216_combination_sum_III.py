class Solution:
    def combinationSum3(self, k, n):
        output = []
        self.dfs(range(1,10), output, [], k, n)
        return output
        
    def dfs(self, nums, output, temp, k, n):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            output.append(temp)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], output, temp + [nums[i]], k - 1, n - nums[i])

# Alternative solution

class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        self.dfs(k, n, output, 1, [])
        return output
    
    def dfs(self, k, n, output, nxt, path):
        if k == 0:
            if n == 0:
                output.append(path)
            return
        for i in range(nxt, 10):
            self.dfs(k - 1, n - i, output, i + 1, path + [i])
