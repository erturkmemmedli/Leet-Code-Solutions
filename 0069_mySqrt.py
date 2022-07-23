class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (right + left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                right = mid - 1
            if mid ** 2 < x:
                left = mid + 1
        if left ** 2 > x: return left - 1
        if right ** 2 < x: return right
        return x

# Alternative solution

class Solution1:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)
