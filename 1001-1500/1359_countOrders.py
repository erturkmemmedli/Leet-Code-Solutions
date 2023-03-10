class Solution:
    def countOrders(self, n: int) -> int:
        total = 1
        for i in range(1, n + 1):
            space = (i - 1) * 2 + 1
            count = space * (space + 1) // 2
            total *= count
            total %= 1_000_000_007
        return total
