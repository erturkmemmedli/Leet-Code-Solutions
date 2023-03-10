class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.result = []
        self.backtrack(num)
        return self.result

    def backtrack(self, num):
        if not num and len(self.result) > 2 and self.result[-1] < 2**31:
            return True
        if len(self.result) < 2:
            for i in range(1, len(num)//2+1):
                nextFibo = int(num[:i])
                if i == 1 or (i > 1 and num[0] != '0') and nextFibo < 2**31:
                    self.result.append(nextFibo)
                    if self.backtrack(num[i:]):
                        return True
                    else:
                        self.result.pop()
        else:
            for i in range(len(str(self.result[-1])), len(num)+1):
                nextFibo = int(num[:i])
                if (i == 1 or (i > 1 and num[0] != '0')) and nextFibo == self.result[-1] + self.result[-2] and nextFibo < 2**31:
                    self.result.append(nextFibo)
                    if self.backtrack(num[i:]):
                        return True
                    else:
                        self.result.pop()
