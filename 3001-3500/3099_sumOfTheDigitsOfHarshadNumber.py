class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digit = sum(int(i) for i in str(x))
        return sum_of_digit if x % sum_of_digit == 0 else -1
