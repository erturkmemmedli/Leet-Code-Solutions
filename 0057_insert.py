class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] < newInterval[0]:
                result.append(intervals[i])
                i += 1
            else:
                break
        if result and newInterval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], newInterval[1])
        else:
            result.append(newInterval)
        for current in intervals[i:]:
            last = result[-1]
            if current[0] > last[1]:
                result.append(current)
            else:
                start = last[0]
                end = max(last[1], current[1])
                result[-1] = [start, end]
        return result    
