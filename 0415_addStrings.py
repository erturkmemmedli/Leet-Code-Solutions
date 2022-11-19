class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) != len(num2):
            num1, num2 = max(num1, num2, key = len), min(num1, num2, key = len) 
        remain = 0
        i = len(num1) - 1
        result = ""
        k = len(num1) - len(num2)
        while i >= k:
            if ord(num1[i]) + ord(num2[i-k]) + remain - 96 <= 9:
                result += chr(ord(num1[i]) + ord(num2[i-k]) + remain - 48)
                remain = 0
                i -= 1
            else:
                result += chr(ord(num1[i]) + ord(num2[i-k]) + remain - 58)
                remain = 1
                i -= 1
        for j in range(i,-1,-1):
            if remain:
                if num1[j] == '9':
                    result += '0'
                else:
                    result += chr(ord(num1[j]) + remain)
                    remain = 0
            else:
                result += num1[j]
        if remain:
            result += '1'
        return result[::-1]
