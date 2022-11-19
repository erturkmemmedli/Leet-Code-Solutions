class Solution:
    def isHappy(self, n: int) -> bool:
        Set = set()
        while n not in Set:
            Set.add(n)
            num = str(n)
            x = 0
            for i in num:
                x += int(i) ** 2
            n = x
        return n == 1
