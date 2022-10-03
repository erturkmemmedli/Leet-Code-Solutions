class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        for prime in primes:
            heapq.heappush(heap, (prime, prime, 0))
        factors = [1] * n
        i = 1
        while i < n:
            new_element, prime, index = heapq.heappop(heap)
            if new_element != factors[i - 1]:
                factors[i] = new_element
                i += 1
            heapq.heappush(heap, (prime * factors[index + 1], prime, index + 1))
        return factors[-1]
