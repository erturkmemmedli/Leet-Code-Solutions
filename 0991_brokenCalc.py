class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        totalOperation = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
                totalOperation += 1
            else:
                target += 1
                totalOperation += 1
        totalOperation += startValue - target
        return totalOperation
