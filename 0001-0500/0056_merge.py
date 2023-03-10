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

# Alternative solution

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        for current in intervals[1:]:
            last = result[-1]
            if last[1] >= current[0]: 
                start = last[0]
                end = max(current[1], last[1])
                result[-1] = [start, end]
            else:
                result.append(current)
        return result
