class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[0],-x[1]])
        count = 0
        x, y = intervals[0]
        for i, [a, b] in enumerate(intervals[1:]):
            if x <= a and b <= y:
                count += 1
            else:
                x, y = a, b
        return len(intervals) - count
