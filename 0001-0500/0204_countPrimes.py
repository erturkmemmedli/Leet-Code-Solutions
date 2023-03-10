class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        nonprimes = self.isPrime(n, set())
        return n - len(nonprimes) - 2
    
    def isPrime(self, n, s):
        for i in range(2, int(n**0.5)+1):
            if i not in s:
                for j in range(i*i, n, i):
                    s.add(j)
        return s
        
# Alternative solution

class Solution1:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        l = [True] * n
        l[0] = l[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if l[i]:
                for j in range(i*i, n, i):
                    l[j] = False
        return sum(l)
        
# Alternative solution

class Solution2:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        l = [True] * n
        l[0] = l[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if l[i]:
                l[i*i:n:i] = [False] * len(l[i*i:n:i])
        return sum(l)
