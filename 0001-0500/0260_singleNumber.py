from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        C = Counter(nums)
        return [key for key, val in C.items() if val == 1]

# Alternative solution

class Solution1:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        step = 1
        while xor & step == 0:
            step <<= 1
        first = 0
        second = 0
        for num in nums:
            if num & step:
                first ^= num
            else:
                second ^= num
        return [first, second]
