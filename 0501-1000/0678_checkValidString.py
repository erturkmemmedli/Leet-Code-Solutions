class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            if char == ')':
                low = low - 1 if low > 0 else 0
                high -= 1
            if char == '*':
                high += 1
                low = low - 1 if low > 0 else 0
            if high < 0:
                return False
        return low == 0
