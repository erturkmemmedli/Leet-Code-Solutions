class Solution:
    def findNthDigit(self, n: int) -> int:
        indicator = 9
        multiplier = 1

        while n > indicator * multiplier:
            n -= indicator * multiplier
            indicator *= 10
            multiplier += 1
        
        start = 10 ** (multiplier - 1)
        increase, index = divmod(n, multiplier)
        print(start, increase, index)
        
        return int(str(start + increase - (0 if increase % 10 == 0 and index != 0 else 1))[index - 1])
