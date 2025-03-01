class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum([1 for i in nums if i < k])
