class Solution:
    def baseNeg2(self, n: int) -> str:
        result = ""
        while n:
            result += str(n & 1)
            n = -(n >> 1)
        return result[::-1] if result else "0"
