from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        C = Counter(nums)
        return [key for key, val in C.items() if val == 1]
