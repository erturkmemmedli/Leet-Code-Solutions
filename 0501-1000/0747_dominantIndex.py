class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = second = -inf
        idx = None

        for i, num in enumerate(nums):
            if num > first:
                second = first
                first = num
                idx = i
            elif num > second:
                second = num
            
        return idx if first >= second * 2 else -1
