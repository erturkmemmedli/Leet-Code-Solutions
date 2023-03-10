class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maximums = []
        for i, val in enumerate(values):
            if i == 0:
                maximums.append(val)
            else:
                maximums.append(max(maximums[-1], i + val))
        mxm = values[0] + values[1] - 1
        for i in range(2, len(values)):
            mxm = max(mxm, maximums[i-1] + values[i] - i)
        return mxm
