class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = ""
        while a and b and a != b:
            if a > b:
                result += 2 * 'a' + 'b'
                a -= 2
                b -= 1
            else:
                result += 2 * 'b' + 'a'
                b -= 2
                a -= 1
        if a and b:
            result += a * 'ab'
        elif a:
            result += a * 'a'
        elif b:
            result += b * 'b'
        return result
