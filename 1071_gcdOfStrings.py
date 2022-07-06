class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) != len(str2):
            str1, str2 = max(str1, str2, key = len), min(str1, str2, key = len)
        a = len(str1)
        b = len(str2)
        l = self.gcd(a, b)
        if str1[:l] != str2[:l]:
            return ""
        else:
            part = str1[:l]
        for i in range(0, b, l):
            if str1[i:i+l] != part or str2[i:i+l] != part:
                return ""
        for i in range(b, a, l):
            if str1[i:i+l] != part:
                return ""
        return part
        
    def gcd(self, a, b):
        while True:
            if a % b == 0:
                return b
            a, b = b, a % b
