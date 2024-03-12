class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        max_prime = 0

        def is_prime(number):
            if number < 2:
                return False
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    return False
            return True

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j or i + j == len(nums) - 1:
                    if is_prime(nums[i][j]):
                        max_prime = max(max_prime, nums[i][j])

        return max_prime
