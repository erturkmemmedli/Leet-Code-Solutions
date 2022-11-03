class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result, move = 0, 0
        for num in nums:
            result += max(move - num, 0)
            move = max(move + 1, num + 1)
        return result

# Alternatie solution (which gives TLE error)

class Solution1:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        available = sorted(list(set(range(1, max(nums) + len(nums))) - set(nums)))
        nums.sort()
        visited = set()
        result = 0
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                index = bisect.bisect_right(available, num)
                available = available[index:]
                result += available[0] - num
                available = available[1:]
        return result
