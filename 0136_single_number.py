class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# Alternative solution

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.discard(num)
        return s.pop()
