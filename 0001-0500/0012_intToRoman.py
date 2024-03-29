class Solution:
    def calculation(self, roman, num, big, mid, small):
        if num == 9:
            roman += small + big
        elif num >= 5:
            roman += mid + small * (num - 5)
        elif num == 4:
            roman += small + mid
        else:
            roman += small * num
        return roman
    
    def intToRoman(self, num: int) -> str:
        number = str(num)
        power = len(number) - 1
        roman = ""
        for i in range(power + 1):
            if power - i >= 3:
                roman += 'M' * (int(number[i]) * 10 ** power // 10 ** 3)
            elif power - i == 2:
                roman = self.calculation(roman, int(number[i]), 'M', 'D', 'C')
            elif power - i == 1:
                roman = self.calculation(roman, int(number[i]), 'C', 'L', 'X')
            else:
                roman = self.calculation(roman, int(number[i]), 'X', 'V', 'I')
        return roman
    
# Alternative solution

class Solution1:
    def intToRoman(self, num: int) -> str:
        Map = {1000: 'M', 900: 'CM', 500: 'D',
               400: 'CD', 100: 'C', 90: 'XC',
               50: 'L', 40: 'XL', 10: 'X',
               9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        roman = ""
        for key, val in Map.items():
            if num >= key:
                coeff = num // key
                num = num % key
                roman += coeff * val
        return roman
