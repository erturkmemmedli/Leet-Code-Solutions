class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[0], x[1]])
        deleted = 0
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            if left < end:
                if right >= end:
                    deleted += 1
                else:
                    start = left
                    end = right
                    deleted += 1
            else:
                start = left
                end = right
        return deleted
