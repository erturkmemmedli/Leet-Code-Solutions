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

# Alternative solition

class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(n, k, result, 1, [])
        return result
    
    def backtrack(self, n, k, result, nxt, temp):
        if k == 0:
            result.append(temp)
            return
        else:
            for i in range(nxt, n + 1):
                self.backtrack(n, k - 1, result, i + 1, temp + [i])
                
# Alternative solution

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(n, k, result, 1, [])
        return result
    
    def backtrack(self, n, k, result, nxt, temp):
        if k == 0:
            result.append(temp.copy())
            return
        else:
            for i in range(nxt, n + 1):
                temp.append(i)
                self.backtrack(n, k - 1, result, i + 1, temp)
                temp.pop()
