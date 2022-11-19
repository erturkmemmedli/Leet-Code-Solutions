class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        product = 1
        for digit in digits:
            product *= digit
        summ = sum(digits)
        return product - summ
