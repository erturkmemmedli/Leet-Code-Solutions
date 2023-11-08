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

# Alternative solution

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        merged_schedule = schedule[0]
        output = []

        for i in range(1, len(schedule)):
            merged_schedule = self.merge_intervals(merged_schedule, schedule[i])

        for i in range(1, len(merged_schedule)):
            output.append(Interval(merged_schedule[i-1].end, merged_schedule[i].start))

        return output


    def merge_intervals(self, first, second):
        result = []
        i = j = 0

        while i < len(first) and j < len(second):
            if first[i].start > second[j].end:
                result.append(second[j])
                j += 1
            
            elif first[i].end < second[j].start:
                result.append(first[i])
                i += 1
            
            elif first[i].end > second[j].end:
                first[i].start = min(first[i].start, second[j].start)
                first[i].end = max(first[i].end, second[j].end)
                j += 1

            else:
                second[j].start = min(first[i].start, second[j].start)
                second[j].end = max(first[i].end, second[j].end)
                i += 1

        while i < len(first):
            result.append(first[i])
            i += 1

        while j < len(second):
            result.append(second[j])
            j += 1   

        return result  
