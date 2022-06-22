class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
      
# Alternative solution

class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) != len(b):
            a, b = max(a, b, key = len), min(a, b, key = len)
            b = (len(a) - len(b)) * '0' + b
        result = ""
        i = len(a) - 1
        remember = '0'
        while i >= 0:
            if a[i] == '0' and b[i] == '0':
                result += remember
                remember = '0'
            elif a[i] == '1' and b[i] == '1':
                result += remember
                remember = '1'
            else:
                if remember == '0':
                    result += '1'
                if remember == '1':
                    result += '0'
            i -= 1
        if remember == '1': result += remember
        return result[::-1]
