class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i, height in enumerate(heights):
            if expected[i] != height:
                count += 1
        return count

# Alternative solution

class Solution1:
    def heightChecker(self, heights: List[int]) -> int:
        counting_array = [0] * 100
        for h in heights:
            counting_array[h-1] += 1
        expected = []
        for i, c in enumerate(counting_array):
            if c: expected += [i+1] * c
        count = 0
        for he, ex in zip(heights, expected):
            if he != ex: count += 1
        return count
