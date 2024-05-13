class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        maximum = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            elif nums[j] == nums[i] + 1:
                maximum = max(maximum, j - i + 1)
                j += 1
            else:
                while i < j:
                    if nums[j] - nums[i] <= 1:
                        break
                    i += 1
                j += 1
        return maximum

# Alternative solution

from collections import Counter

class Solution1:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        c = sorted(c.items())
        out = 0
        for i in range(1, len(c)):
            if c[i][0] - c[i-1][0] == 1:
                out = max(out, c[i][1] + c[i-1][1])
        return out

# Alternative solution

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_map = {}
        length = 0

        num_map = Counter(nums)
            
        for key in sorted(num_map.keys()):
            if key - 1 in num_map:
                a = num_map[key]
                b = num_map[key - 1]

                length = max(length, a + b)
        
        return length
