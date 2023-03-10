class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left << 1 < right:
            return 0
        for num in range(left + 1, min(right + 1, left << 1 + 1)):
            left &= num
            if left == 0:
                return 0
        return left
