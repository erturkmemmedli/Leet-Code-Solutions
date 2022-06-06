class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
      
# Alternative solution

from math import floor, log10

class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (floor(log10(num)) + 1) % 2 == 0:
                count += 1
        return count
