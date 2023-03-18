class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        max_horizontal_distance = max(h - horizontalCuts[-1], horizontalCuts[0])
        for i in range(1, len(horizontalCuts)):
            max_horizontal_distance = max(max_horizontal_distance, horizontalCuts[i] - horizontalCuts[i - 1])

        verticalCuts.sort()
        max_vertical_distance = max(w - verticalCuts[-1], verticalCuts[0])
        for i in range(1, len(verticalCuts)):
            max_vertical_distance = max(max_vertical_distance, verticalCuts[i] - verticalCuts[i - 1])

        return max_horizontal_distance * max_vertical_distance % 1_000_000_007
