class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            minutes.append(int(time[:2]) * 60 + int(time[-2:]))
        minutes.sort()
        minutes.append(minutes[0] + 1440)
        diff = float('INF')
        for i in range(1, len(minutes)):
            diff = min(diff, minutes[i] - minutes[i-1])
        return diff
