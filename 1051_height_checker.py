class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i, height in enumerate(heights):
            if expected[i] != height:
                count += 1
        return count
