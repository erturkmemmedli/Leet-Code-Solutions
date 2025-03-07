class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        numbers = set(range(2, right + 1))

        for i in range(2, int(right ** 0.5) + 1):
            if i in numbers:
                for j in range(i * i, right + 1, i):
                    numbers.discard(j)
        
        primes = sorted(list(numbers))

        for i in range(len(primes)):
            if primes[i] < left:
                continue
            else:
                primes = primes[i:]
                break
        else:
            primes = []

        if len(primes) < 2:
            return [-1, -1]
        
        gap = math.inf
        answer = [None, None]

        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < gap:
                gap = primes[i] - primes[i - 1]
                answer = [primes[i - 1], primes[i]]

        return answer
