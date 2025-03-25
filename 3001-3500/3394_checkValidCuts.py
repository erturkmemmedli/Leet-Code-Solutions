class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_coords = []
        y_coords = []

        for x1, y1, x2, y2 in rectangles:
            x_coords.append([x1, x2])
            y_coords.append([y1, y2])

        def merge_interval(intervals):
            intervals.sort()
            merged_intervals = [intervals[0]]

            for i in range(1, len(intervals)):
                if intervals[i][0] < merged_intervals[-1][1]:
                    merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
                else:
                    merged_intervals.append(intervals[i])

            return merged_intervals

        if len(merge_interval(x_coords)) > 2:
            return True
        
        if len(merge_interval(y_coords)) > 2:
            return True

        return False
