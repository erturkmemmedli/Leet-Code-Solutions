class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp = self.theSieveOfEratosthenes(n)
        primes = [i for i in dp if i != float('inf')]
        for i in range(2, n+1):
            if i in primes:
                continue
            for prime in primes:
                if prime > i:
                    break
                if i % prime == 0:
                    dp[i] = min(dp[i], dp[i // prime] + dp[prime])
        return dp[-1]

    def theSieveOfEratosthenes(self, n):
        table = [i if i % 2 == 1 else float('inf') for i in range(0, n+1)]
        table[1], table[2] = float('inf'), 2
        for i in range(3, int(n ** 0.5)+1):
            if table[i] == float('inf'):
                continue
            else:
                for j in range(i, n-i+1, i):
                    table[j+i] = float('inf')
        return table

# Alternative solution

class Solution1:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return i + self.minSteps(n//i)
        return n
