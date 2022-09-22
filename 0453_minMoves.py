class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        result = 0
        for num in nums:
            result += num - minimum
        return result
