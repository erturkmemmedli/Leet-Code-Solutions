class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if ay1 > by2 or by1 > ay2 or ax1 > bx2 or bx1 > ax2:
            return total
        xs = sorted([ax1, ax2, bx1, bx2])
        ys = sorted([ay1, ay2, by1, by2])
        return total - abs(ys[1] - ys[2]) * abs(xs[1] - xs[2])
