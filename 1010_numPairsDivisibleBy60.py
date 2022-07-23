class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        pre_calculation = [0] * 60
        for t in time:
            index = t % 60
            count += pre_calculation[(60 - index) % 60]
            pre_calculation[index] += 1
        return count
