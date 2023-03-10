from heapq import heappush, heappop

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacciHeap = [1]
        fib1 = 1
        fib2 = 1
        while fib1+ fib2 <= k:
            fib2, fib1 = fib1 + fib2, fib2
            heappush(fibonacciHeap, -fib2)
        total_operation = 0
        while fibonacciHeap:
            pop = -heappop(fibonacciHeap)
            if pop <= k:
                k -= pop
                total_operation += 1
            if k == 0:
                break
        return total_operation
