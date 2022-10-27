class Solution:
    def __init__(self):
        self.output = []

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lowStr = str(low)
        highStr = str(high)
        lowLen = len(lowStr)
        highLen = len(highStr)
        if lowLen == highLen:
            if 10 - int(lowStr[0]) < lowLen:
                return self.output
            else:
                self.helper(low, lowStr, lowLen, high)
        else:
            self.helper(low, lowStr, lowLen, high)
            self.sequentialDigits(int('1' + '0' * lowLen), high)
        return self.output

    def helper(self, low, lowStr, lowLen, high):
        start = lowStr[0]
        for _ in range(10 - int(lowStr[0]) - lowLen + 1):
            numStr = start
            for _ in range(lowLen - 1):
                numStr += str(int(numStr[-1]) + 1)
            num = int(numStr)
            if low <= num <= high:
                self.output.append(num)
            start = str(int(start) + 1)
