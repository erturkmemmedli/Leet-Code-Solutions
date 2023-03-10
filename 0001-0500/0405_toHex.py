class Solution:
    def toHex(self, num: int) -> str:
        d = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        for i in range(10):
            d[i] = str(i)
        result = ""
        if num >= 0:
            while num or not result:
                result += d[num % 16]
                num = num // 16
            return result[::-1]
        else:
            p = 0
            x = 0
            while x + num < 0:
                x = 16 ** p
                p += 1
            output = 'f' * (8 - p + 1)
            num = x + num
            if num == 0:
                return output
            while num or not result:
                result += d[num % 16]
                num = num // 16
            return output + result[::-1]
