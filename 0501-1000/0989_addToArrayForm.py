class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        remember = 0
        index = len(num) - 1
        while k:
            digit = k % 10
            if index >= 0:
                num[index] += digit + remember
                if num[index] >= 10:
                    num[index] %= 10
                    remember = 1
                else:
                    remember = 0
            else:
                add = digit + remember
                if add >= 10:
                    add %= 10
                    remember = 1
                else:
                    remember = 0
                num.insert(0, add)
            k //= 10
            index -= 1
        if remember:
            while index >= 0 and remember:
                num[index] += remember
                if num[index] >= 10:
                    num[index] %= 10
                    remember = 1
                else:
                    remember = 0
                index -= 1
        if remember:
            num.insert(0, 1)
        return num
