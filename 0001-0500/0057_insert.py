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

# Alternative solution

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        left = self.binarySearch(intervals, newInterval[0], True)
        right = self.binarySearch(intervals, newInterval[1], False)
        print(left, right)
        start = min((intervals[left][0] if left < len(intervals) else intervals[-1][0]), newInterval[0])
        end = max((intervals[right][1] if right < len(intervals) else intervals[-1][1]), newInterval[1])
        return intervals[:left] + [[start, end]] + intervals[right + 1:]

    def binarySearch(self, intervals, target, flag):
        left, right = 0, len(intervals) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][0] > target:
                right = mid - 1
            elif intervals[mid][1] < target:
                left = mid + 1
            else:
                return mid
        return left if flag else right

# Alternative solution

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = self.binary_search(intervals, newInterval[0], True)
        right = self.binary_search(intervals, newInterval[1], False)
        
        final_intervals = []

        for i in range(left):
            final_intervals.append(intervals[i])
        
        if right >= left:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right][1])

        final_intervals.append(newInterval)

        for i in range(right + 1, len(intervals)):
            final_intervals.append(intervals[i])

        return final_intervals


    def binary_search(self, intervals, target, is_left):
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if intervals[mid][0] <= target <= intervals[mid][1]:
                return mid

            elif intervals[mid][0] > target:
                right = mid - 1

            else:
                left = mid + 1
            
        return left if is_left else right

# Alternative solution

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low, high = newInterval

        def binary_search(target, cond):
            left = 0
            right = len(intervals) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if intervals[mid][0] <= target <= intervals[mid][1]:
                    return mid if cond else mid + 1
                elif intervals[mid][0] > target:
                    right = mid - 1
                elif intervals[mid][1] < target:
                    left = mid + 1
            
            return left
        
        start = binary_search(low, True)
        end = binary_search(high, False)

        return intervals[:start] + [newInterval if start == end else [min(low, intervals[start][0]), max(high, intervals[end-1][1])]] + intervals[end:]
