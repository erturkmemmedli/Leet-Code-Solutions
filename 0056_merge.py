class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        answer = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                answer.append([start, end])
                start, end = intervals[i]
            elif intervals[i][0] <= end and intervals[i][1] > end:
                end = intervals[i][1]
            elif intervals[i][0] <= end and intervals[i][1] <= end:
                continue
        answer.append((start, end))
        return answer
