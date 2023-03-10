class Solution:
    def splitNum(self, num: int) -> int:
        numStr = str(num)
        arr = sorted(list(numStr), reverse = True)
        num1 = ""
        num2 = ""
        while arr:
            if len(num1) == len(num2):
                num1 += arr.pop()
            else:
                num2 += arr.pop()
        return int(num1) + int(num2)
