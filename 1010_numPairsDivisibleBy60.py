class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        pre_calculation = [0] * 60
        for t in time:
            index = t % 60
            count += pre_calculation[(60 - index) % 60]
            pre_calculation[index] += 1
        return count

# Alternative solution

class Solution1:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hourlyInterval = [0] * 60
        pairs = 0
        for t in time:
            hourlyInterval[t % 60] += 1
        x, y = hourlyInterval[0], hourlyInterval[30]
        pairs += x * (x-1) // 2 + y * (y-1) // 2
        for i in range(1, 30):
            a, b = hourlyInterval[i], hourlyInterval[60-i]
            pairs += a * b
        return pairs
