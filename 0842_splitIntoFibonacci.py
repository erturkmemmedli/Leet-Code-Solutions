class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.result = []
        self.backtrack(num)
        return self.result

    def backtrack(self, num):
        if not num and len(self.result) > 2 and self.result[-1] < 2**31:
            return True
        if len(self.result) > 2 and len(str(self.result[-1])) > len(num):
            return False
        if len(self.result) < 2:
            for i in range(1, len(num)//2+1):
                if i == 1 or (i > 1 and num[0] != '0'):
                    self.result.append(int(num[:i]))
                    if self.backtrack(num[i:]):
                        return True
                    else:
                        self.result.pop()
        else:
            for i in range(len(str(self.result[-1])), len(num)+1):
                nextFibonacciNumber = int(num[:i])
                if (i == 1 or (i > 1 and num[0] != '0')) and nextFibonacciNumber == self.result[-1] + self.result[-2]:
                    self.result.append(nextFibonacciNumber)
                    if self.backtrack(num[i:]):
                        return True
                    else:
                        self.result.pop()
