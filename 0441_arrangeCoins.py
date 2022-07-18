class Solution:
    def arrangeCoins(self, n: int) -> int:
        discriminant = 1 + 4 * 2 * n
        root = (discriminant ** 0.5 - 1) / 2
        return int(root)
