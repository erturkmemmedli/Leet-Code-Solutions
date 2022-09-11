class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = duration # last hit is added in advance
        for i in range(len(timeSeries) - 1):
            if timeSeries[i+1] - timeSeries[i] > duration:
                total += duration
            else:
                total += timeSeries[i+1] - timeSeries[i]
        return total
