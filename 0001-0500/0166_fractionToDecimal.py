class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            negative_flag = True
        else:
            negative_flag = False

        numerator = abs(numerator)
        denominator = abs(denominator)

        val_set ={}
        result = ""

        if numerator >= denominator:
            result += str(numerator // denominator) + "."
            numerator %= denominator
        else:
            result += "0."
        numerator *= 10

        while numerator:
            if numerator not in val_set:
                val_set[numerator] = len(result)
                if numerator >= denominator:
                    result += str(numerator // denominator)
                    numerator %= denominator
                else:
                    result += "0"
                numerator *= 10
            else:
                idx = val_set[numerator]
                result = result[:idx] + "(" + result[idx:] + ")"
                break
        
        if result[-1] == '.':
            result = result[:-1]

        return result if not negative_flag else '-' + result
