class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        repeated = set()
        result = set()
        for num in nums:
            if num not in result and num not in repeated:
                result.add(num)
                repeated.add(num)
            elif num in repeated:
                result.discard(num)
        return result.pop()
        
# Alternative solution

from collections import Counter

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        return [k for k, v in Counter(nums).items() if v == 1][0]
        
# Alternative solution

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        y = 0
        mask = 0
        for num in nums:
            y ^= x & num
            x ^= num
            mask = ~(x & y)
            y &= mask
            x &= mask
        return x
