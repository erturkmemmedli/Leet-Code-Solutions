class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger: return True
        sumOfIntegers =  maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if sumOfIntegers < desiredTotal: return False
        if sumOfIntegers == desiredTotal: return maxChoosableInteger % 2
        self.visited = {}
        return self.recursiveDP(list(range(1, maxChoosableInteger + 1)), desiredTotal)
        
    def recursiveDP(self, nums, total):
        if nums[-1] >= total:
            return True
        numsTupled = tuple(nums)
        if numsTupled in self.visited:
            return self.visited[numsTupled]
        for i in range(len(nums)):
            if not self.recursiveDP(nums[:i] + nums[i+1:], total - nums[i]):
                self.visited[numsTupled] = True
                return True
        self.visited[numsTupled] = False
        return False
