class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        flag = num < 0
        num = abs(num)
        while num or not result:
            result += str(num % 7)
            num = num // 7
        if flag: result += '-'
        return result[::-1] 
