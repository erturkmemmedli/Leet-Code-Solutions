"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        allIntervals = []
        for intervals in schedule:
            for interval in intervals:
                allIntervals.append(interval)
        allIntervals.sort(key = lambda x: x.start)
        mergedIntervals = [allIntervals[0]]
        start, end = allIntervals[0].start, allIntervals[0].end
        for interval in allIntervals[1:]:
            last = mergedIntervals[-1]
            if interval.start <= last.end:
                start = last.start
                end = max(last.end, interval.end)
                newInterval = Interval(start, end)
                mergedIntervals[-1] = newInterval
            else:
                mergedIntervals.append(interval)
        freeIntervals = []
        for i in range(1, len(mergedIntervals)):
            start = mergedIntervals[i-1].end
            end = mergedIntervals[i].start
            freeTime = Interval(start, end)
            freeIntervals.append(freeTime)
        return freeIntervals
