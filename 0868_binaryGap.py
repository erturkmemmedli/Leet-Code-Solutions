class Solution:
    def binaryGap(self, n: int) -> int:
        result = 0
        flag = False
        count = 0
        while n:
            if n % 2 == 1:
                if flag:
                    result = max(result, count + 1)
                flag = True
                count = 0
                n = n >> 1
            else:
                if flag:
                    count += 1
                n = n >> 1
        return result
