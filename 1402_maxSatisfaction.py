class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[0] >= 0:
            return sum([num * i for i, num in enumerate(satisfaction, 1)])
        if satisfaction[-1] <= 0:
            return 0
        leftZero = bisect.bisect_left(satisfaction, 0)
        rightZero = bisect.bisect_right(satisfaction, 0)
        positiveTotal = sum(satisfaction[rightZero:])
        i = leftZero - 1
        while i >= 0:
            if positiveTotal + satisfaction[i] > 0:
                positiveTotal += satisfaction[i]
                i -= 1
            else:
                break
        return sum([num * j for j, num in enumerate(satisfaction[i+1:], 1)])
