class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(bin(i)[2:].count('1'))
        return ans
        
# Alternative solution

class Solution1:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.count(i))
        return ans
    
    def count(self, n):
        count = 0
        while n:
            count += 1
            n &= n-1
        return count
      
# Alternative solution

class Solution2:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i-1] + 1
        return dp
