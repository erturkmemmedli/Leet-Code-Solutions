class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i ** 0.5 == int(i ** 0.5):
                dp[i] = 1
            else:
                minimum = float('inf')
                for j in squares:
                    if j < i:
                        minimum = min(minimum, dp[j] + dp[i-j])
                    else:
                        break
                dp[i] = minimum
        return dp[n]
      
# Alternative solution

from collections import deque

class Solution1:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        queue = deque([set([n])])
        count = 0
        while queue:
            level = queue.popleft()
            new_level = set()
            for num in level:
                for i in range(1, int(num ** 0.5) + 1):
                    new = num - i ** 2
                    if new == 0:
                        break
                    new_level.add(new)
                if new == 0:
                    break
            if new_level:
                queue.append(new_level)
            count += 1
            if new == 0:
                break
        return count
