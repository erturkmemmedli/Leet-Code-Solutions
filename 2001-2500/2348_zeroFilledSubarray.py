class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = 0
        total = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total += zeros * (zeros + 1) // 2
                zeros = 0
        total += zeros * (zeros + 1) // 2
        return total
